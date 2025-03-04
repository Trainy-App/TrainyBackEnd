from rest_framework import viewsets

from core.trainy.models import Division
from core.trainy.serializers import DivisionSerializer

class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer