from rest_framework import viewsets

from core.trainy.models import Muscles
from core.trainy.serializers import MuscleSerializer


class MuscleViewSet(viewsets.ModelViewSet):
    queryset = Muscles.objects.all()
    serializer_class = MuscleSerializer