from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.routers import DefaultRouter

from core.uploader.views import ImageViewSet

router = DefaultRouter()
router.register(r'images', ImageViewSet)

@api_view(['GET'])
def uploader_root(request, format=None):
    return Response({
        'images': reverse('image-list', request=request, format=format),
    })

urlpatterns = [
    path('', uploader_root, name='uploader-root'),
    path('', include(router.urls)),
]