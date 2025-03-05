from core.trainy.serializers import WorkoutListSerializers
from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.response import Response
from core.trainy.models import Workout, Division, Exercicies_Division, Exercicies
from core.authentication.models import Athlete
from django_filters.rest_framework import DjangoFilterBackend
from core.trainy.filters import WorkoutUserFilter

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutListSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = WorkoutUserFilter

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            athlete_instance = Athlete.objects.get(id=serializer.validated_data["athlete"].id)

            workout_data = {
                "name": serializer.validated_data["name"],
                "description": serializer.validated_data["description"],
                "date": serializer.validated_data["date"],
                "athlete": athlete_instance,
            }

            workout_instance = Workout.objects.create(**workout_data)

            for division_data in serializer.validated_data["divisions"]:
                division_instance = Division.objects.create(
                    name=division_data["name"],
                    workout=workout_instance,
                )

                division_instance.muscles.set(division_data["muscles"])

                for exercise_data in division_data["exercises"]:
                    exercicie_instance = Exercicies.objects.get(id=exercise_data["id_exercicie"])

                    Exercicies_Division.objects.create(
                        exercicie=exercicie_instance,
                        division=division_instance,
                        series=exercise_data["sets"],
                        repetitions=exercise_data["reps"]
                    )

            return Response({"message": "Workout created successfully"}, status=status.HTTP_201_CREATED)

        except Exception as e:
    
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
