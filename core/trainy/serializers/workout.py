from rest_framework import serializers

from core.authentication.models import Athlete
from core.trainy.models import Workout, Division, Exercicies, Muscles, Exercicies_Division
from .division import DivisionSerializer

class ExerciseInputSerializer(serializers.Serializer):
    id_exercicie = serializers.IntegerField()
    sets = serializers.IntegerField()
    reps = serializers.IntegerField()

class DivisionCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    muscles = serializers.ListField(child=serializers.IntegerField())
    exercises = ExerciseInputSerializer(many=True)

class WorkoutCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(allow_blank=True, required=False)
    date = serializers.CharField(allow_blank=True, required=False)
    athlete = serializers.PrimaryKeyRelatedField(queryset=Athlete.objects.all())
    divisions = DivisionCreateSerializer(many=True)

class WorkoutListSerializers(serializers.ModelSerializer):
    athlete = serializers.PrimaryKeyRelatedField(queryset=Athlete.objects.all())

    class Meta:
        model = Workout
        fields = "__all__"

class WorkoutDetailSerializer(serializers.ModelSerializer):
    athlete = serializers.PrimaryKeyRelatedField(queryset=Athlete.objects.all())
    divisions = DivisionSerializer(many=True)

    class Meta:
        model = Workout
        fields = "__all__"


class MusclesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muscles
        fields = ['id', 'name', 'description']

class ExerciseOutputSerializer(serializers.ModelSerializer):
    muscle = MusclesListSerializer(many=True)

    class Meta:
        model = Exercicies
        fields = ['id', 'name', 'description', 'muscle']

class DivisionListSerializer(serializers.ModelSerializer):
    exercises = serializers.SerializerMethodField()
    muscles = MusclesListSerializer(many=True)

    class Meta:
        model = Division
        fields = ['id', 'name', 'muscles', 'exercises']

    def get_exercises(self, obj):

        exercicies_division = Exercicies_Division.objects.filter(division=obj)
        exercises = [exercicie.exercicie for exercicie in exercicies_division]
        return ExerciseOutputSerializer(exercises, many=True).data



class WorkoutListSerializers(serializers.ModelSerializer):
    athlete = serializers.PrimaryKeyRelatedField(queryset=Athlete.objects.all())
    divisions = DivisionListSerializer(many=True)

    class Meta:
        model = Workout
        fields = ['id', 'name', 'date', 'description', 'athlete', 'divisions']