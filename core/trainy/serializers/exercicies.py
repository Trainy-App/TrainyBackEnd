from rest_framework import serializers
from core.trainy.models import Exercicies

class ExerciciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercicies
        fields = '__all__'