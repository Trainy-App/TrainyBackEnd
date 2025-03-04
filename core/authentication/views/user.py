import http
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
from core.authentication.serializers import AthleteSerializer, PersonalSerializer
from django_filters.rest_framework import DjangoFilterBackend

User = get_user_model()



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

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
        user = request.user

        if request.method == 'GET':
            serializer = self.get_serializer(user)
            return Response(serializer.data)

        elif request.method == 'PATCH':
            user = request.user
            if hasattr(user, 'athlete'):
                serializer = AthleteSerializer(user.athlete, data=request.data, partial=True)
            elif hasattr(user, 'personal'):
                serializer = PersonalSerializer(user.personal, data=request.data, partial=True)
            else:
                serializer = self.get_serializer(user, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            try:
                user.delete()
                return Response({"detail": "Conta deletada com sucesso"}, status=status.HTTP_204_NO_CONTENT)
            except Exception:
                return Response({"error": "Erro ao deletar conta"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"error": "Método não permitido"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


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
        # Se os relacionamentos forem OneToOne, use select_related;
        # caso contrário, prefetech_related com o nome correto da relação.
        users = User.objects.all().select_related('personal', 'athlete')
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
        

    def retrieve(self, request, *args, **kwargs):
        """Bloqueia busca de usuário por ID"""
        raise PermissionDenied("Use /api/users/me/ para acessar seus dados")
    
    def create(self, request, *args, **kwargs):
        """Bloqueia criação de usuários"""
        raise PermissionDenied("Operação não permitida")

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
