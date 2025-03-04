from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.routers import DefaultRouter

from core.trainy.views import (
    WorkoutViewSet,
    DivisionViewSet,
    ExerciciesDivisionViewSet,
    MuscleViewSet,
    ExerciciesViewSet
)

router = DefaultRouter()
router.register(r'workouts', WorkoutViewSet, basename='workouts')
router.register(r'divisions', DivisionViewSet, basename='divisions')
router.register(r'exercicies_divisions', ExerciciesDivisionViewSet, basename='exercicies_divisions')
router.register(r'muscles', MuscleViewSet, basename='muscles')
router.register(r'exercicies', ExerciciesViewSet, basename='exercicies')

@api_view(['GET'])
def trainy_root(request, format=None):
    return Response({
        'workouts': reverse('workouts-list', request=request, format=format),
        'divisions': reverse('divisions-list', request=request, format=format),
        'exercicies_divisions': reverse('exercicies_divisions-list', request=request, format=format),
        'muscles': reverse('muscles-list', request=request, format=format),
        'exercicies': reverse('exercicies-list', request=request, format=format)
    })

urlpatterns = [
    path('', trainy_root, name='trainy-root'),
    path('', include(router.urls)),
]