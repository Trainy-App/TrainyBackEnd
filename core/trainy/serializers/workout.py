from rest_framework import serializers

from core.authentication.models import Athlete
from core.trainy.models import Workout, Division, Exercicies, Muscles, Exercicies_Division
from .division import DivisionSerializer

class ExerciseSerializer(serializers.Serializer):
    id_exercicie = serializers.IntegerField()
    sets = serializers.IntegerField()
    reps = serializers.IntegerField()

class DivisionCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    muscles = serializers.ListField(child=serializers.IntegerField())
    exercises = ExerciseSerializer(many=True)

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
    divisions = DivisionSerializer(many=True)  # Serializando as divisões corretamente

    class Meta:
        model = Workout
        fields = "__all__"  # Inclui todos os campos do modelo Workout, incluindo as divisões


class MusclesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muscles
        fields = ['id', 'name', 'description']

class ExerciseSerializer(serializers.ModelSerializer):
    muscle = MusclesListSerializer(many=True)  # Serializando os músculos relacionados ao exercício

    class Meta:
        model = Exercicies
        fields = ['id', 'name', 'description', 'muscle']

class DivisionListSerializer(serializers.ModelSerializer):
    exercises = serializers.SerializerMethodField()  # Use a custom method to get exercises
    muscles = MusclesListSerializer(many=True)  # Serializing the muscles of the division

    class Meta:
        model = Division
        fields = ['id', 'name', 'muscles', 'exercises']

    def get_exercises(self, obj):
        # Retrieving the exercises related to this division using the intermediary model
        exercicies_division = Exercicies_Division.objects.filter(division=obj)
        exercises = [exercicie.exercicie for exercicie in exercicies_division]  # Get the exercises
        return ExerciseSerializer(exercises, many=True).data  # Serialize and return the exercises



class WorkoutListSerializers(serializers.ModelSerializer):
    athlete = serializers.PrimaryKeyRelatedField(queryset=Athlete.objects.all())
    divisions = DivisionListSerializer(many=True)  # Serializando as divisões com seus exercícios e músculos

    class Meta:
        model = Workout
        fields = ['id', 'name', 'date', 'description', 'athlete', 'divisions']