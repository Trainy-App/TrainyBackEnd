from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from core.authentication.views import CustomTokenObtainPairView

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'authentication': reverse('authentication-root', request=request, format=format),
        #'trainy': reverse('trainy-root', request=request, format=format),
        'uploader': reverse('uploader-root', request=request, format=format),
    })

from core.authentication.views import (
    CustomTokenObtainPairView, 
    UserViewSet, 
    AthleteViewSet, 
    PersonalViewSet
)

from core.trainy.views import (
    WorkoutViewSet,
    DivisionViewSet,
    ExerciciesDivisionViewSet,
    MuscleViewSet,
    ExerciciesViewSet
)

from core.uploader.views import ImageViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'athletes', AthleteViewSet)
router.register(r'personals', PersonalViewSet)
router.register(r'images', ImageViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'divisions', DivisionViewSet)
router.register(r'exercicies_divisions', ExerciciesDivisionViewSet)
router.register(r'muscles', MuscleViewSet)
router.register(r'exercicies', ExerciciesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/authentication/', include('core.authentication.urls')),
    #path('api/trainy/', include('core.trainy.urls')),
    path('api/uploader/', include('core.uploader.urls')),
    path('', lambda request: redirect('api/', permanent=True)),
]
