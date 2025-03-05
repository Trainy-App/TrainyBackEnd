from rest_framework import serializers
from core.trainy.models import Division, Muscles, Workout

class DivisionSerializer(serializers.ModelSerializer):
    muscles = serializers.PrimaryKeyRelatedField(queryset=Muscles.objects.all(), many=True)
    workout = serializers.PrimaryKeyRelatedField(queryset=Workout.objects.all())
    class Meta:
        model = Division
        fields = ['id', 'name', 'muscles', 'workout']
