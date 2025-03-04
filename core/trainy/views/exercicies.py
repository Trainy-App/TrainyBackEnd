from rest_framework import viewsets

from core.trainy.models import Exercicies
from core.trainy.serializers import ExerciciesSerializer

class ExerciciesViewSet(viewsets.ModelViewSet):
    queryset = Exercicies.objects.all()
    serializer_class = ExerciciesSerializer