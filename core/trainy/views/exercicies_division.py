from rest_framework import viewsets

from core.trainy.models import Exercicies_Division
from core.trainy.serializers import ExerciciesDivisionSerializer

class ExerciciesDivisionViewSet(viewsets.ModelViewSet):
    queryset = Exercicies_Division.objects.all()
    serializer_class = ExerciciesDivisionSerializer