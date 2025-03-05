from rest_framework import serializers
from core.trainy.models import Muscles

class MuscleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muscles
        fields = '__all__'

class MusclesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muscles
        fields = ['id', 'name', 'description']