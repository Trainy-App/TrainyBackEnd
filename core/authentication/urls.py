from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.routers import DefaultRouter

from core.authentication.views import AthleteViewSet, PersonalViewSet, UserViewSet

router = DefaultRouter()
router.register(r'athletes', AthleteViewSet)
router.register(r'personals', PersonalViewSet)
router.register(r'users', UserViewSet)

@api_view(['GET'])
def authentication_root(request, format=None):
    return Response({
        'athletes': reverse('athlete-list', request=request, format=format),
        'personals': reverse('personal-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
    })

urlpatterns = [
    path('', authentication_root, name='authentication-root'),
    path('', include(router.urls)),
]