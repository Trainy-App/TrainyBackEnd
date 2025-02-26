from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from core.authentication.serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from core.authentication.serializers import CustomTokenObtainPairSerializer

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def get_permissions(self):
    #     """Define permissões baseadas na ação da requisição"""
    #     if self.action in ['create']:
    #         return [AllowAny()]
    #     return [IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        """Registra um usuário e retorna o token JWT"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'photo_url': user.photo_url 
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
