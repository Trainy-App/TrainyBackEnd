from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from core.authentication.serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from core.authentication.serializers import CustomTokenObtainPairSerializer
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """Define permissões baseadas na ação da requisição"""
        if self.action in ['create']:
            return [AllowAny()]
        return [IsAuthenticated()]

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

    @action(detail=False, methods=['GET', 'PATCH', 'DELETE'], permission_classes=[IsAuthenticated])
    def me(self, request):
        """Retorna ou atualiza os dados do usuário autenticado"""
        if request.method == 'GET':
            serializer = self.get_serializer(request.user)
            return Response(serializer.data)
        
        elif request.method == 'PATCH':
            serializer = self.get_serializer(request.user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            user = request.user
            user.delete()
            return Response({"detail": "Conta deletada com sucesso"}, status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        """Bloqueia atualização direta via ID"""
        raise PermissionDenied("Use /api/users/me/ para atualizar seus dados")

    def partial_update(self, request, *args, **kwargs):
        """Bloqueia atualização parcial direta via ID"""
        raise PermissionDenied("Use /api/users/me/ para atualizar seus dados")

    def destroy(self, request, *args, **kwargs):
        """Bloqueia deleção de usuários"""
        raise PermissionDenied("Operação não permitida")

    def list(self, request, *args, **kwargs):
        """Bloqueia listagem de usuários"""
        raise PermissionDenied("Operação não permitida")

    def retrieve(self, request, *args, **kwargs):
        """Bloqueia busca de usuário por ID"""
        raise PermissionDenied("Use /api/users/me/ para acessar seus dados")

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
