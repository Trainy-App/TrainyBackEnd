from rest_framework import serializers
from core.trainy.models import Division, Muscles, Workout, Exercicies_Division
from .exercicies import ExerciseInputSerializer
from .exercicies import ExerciseOutputSerializer
from .muscles import MusclesListSerializer


class DivisionSerializer(serializers.ModelSerializer):
    muscles = serializers.PrimaryKeyRelatedField(queryset=Muscles.objects.all(), many=True)
    workout = serializers.PrimaryKeyRelatedField(queryset=Workout.objects.all())
    class Meta:
        model = Division
        fields = ['id', 'name', 'muscles', 'workout']

class DivisionCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    muscles = serializers.ListField(child=serializers.IntegerField())
    exercises = ExerciseInputSerializer(many=True)

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
