from django_filters import rest_framework as filters
from core.trainy.models import Workout

class WorkoutUserFilter(filters.FilterSet):
    athlete_id = filters.NumberFilter(field_name="athlete")

    class Meta:
        model = Workout
        fields = ['athlete_id']
