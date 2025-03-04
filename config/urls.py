from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

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
    path('api/', include(router.urls)),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', lambda request: redirect('api/', permanent=True)),
]
