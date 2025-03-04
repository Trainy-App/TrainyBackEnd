from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from core.authentication.models import Athlete
from core.authentication.serializers import AthleteSerializer



class AthleteViewSet(viewsets.ModelViewSet):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    # permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = AthleteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    