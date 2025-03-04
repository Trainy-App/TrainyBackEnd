from rest_framework import serializers

from core.trainy.models import Exercicies_Division

class ExerciciesDivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercicies_Division
        fields = '__all__'