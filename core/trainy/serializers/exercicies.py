from rest_framework import serializers
from core.trainy.models import Exercicies
from .muscles import MusclesListSerializer

class ExerciciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercicies
        fields = '__all__'

class ExerciseInputSerializer(serializers.Serializer):
    id_exercicie = serializers.IntegerField()
    sets = serializers.IntegerField()
    reps = serializers.IntegerField()

class ExerciseOutputSerializer(serializers.ModelSerializer):
    muscle = MusclesListSerializer(many=True)

    class Meta:
        model = Exercicies
        fields = ['id', 'name', 'description', 'muscle']