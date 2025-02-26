from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', "name"]
        extra_kwargs = {'password': {'write_only': True}} 

    def create(self, validated_data):
        """Cria um usuário e faz o hash da senha corretamente."""
        user = User(**validated_data)
        user.set_password(validated_data['password'])  
        user.save()
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        data['user_id'] = self.user.id
        data['name'] = self.user.name
        data['email'] = self.user.email
        data['username'] = self.user.username

        # Se houver relacionamentos, você pode incluir também
        # if hasattr(self.user, 'profile'):
        #     data['profile'] = {
        #         'bio': self.user.profile.bio,
        #         'image': self.user.profile.image.url if self.user.profile.image else None,
        #     }
        
        return data