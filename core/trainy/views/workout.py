from rest_framework import viewsets

from core.trainy.models import Workout
from core.trainy.serializers.workout import WorkoutSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer