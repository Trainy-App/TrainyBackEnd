from rest_framework import serializers

from core.authentication.models import Athlete
from core.trainy.models import Workout
from .division import DivisionSerializer, DivisionCreateSerializer, DivisionListSerializer
class WorkoutCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(allow_blank=True, required=False)
    date = serializers.CharField(allow_blank=True, required=False)
    athlete = serializers.PrimaryKeyRelatedField(queryset=Athlete.objects.all())
    divisions = DivisionCreateSerializer(many=True)

class WorkoutDetailSerializer(serializers.ModelSerializer):
    athlete = serializers.PrimaryKeyRelatedField(queryset=Athlete.objects.all())
    divisions = DivisionSerializer(many=True)

    class Meta:
        model = Workout
        fields = "__all__"

class WorkoutListSerializers(serializers.ModelSerializer):
    athlete = serializers.PrimaryKeyRelatedField(queryset=Athlete.objects.all())
    divisions = DivisionListSerializer(many=True)

    class Meta:
        model = Workout
        fields = ['id', 'name', 'date', 'description', 'athlete', 'divisions']