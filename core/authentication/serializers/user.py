from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from core.uploader.utils.create_image import create_image 

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    profile_picture = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'name', 'profile_picture', 'photo_url']
        extra_kwargs = {'password': {'write_only': True}} 

    def create(self, validated_data):
        """Cria um usuário, faz o hash da senha e salva a foto de perfil."""
        profile_picture = validated_data.pop('profile_picture', None)

        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        # Se houver uma imagem, fazer o upload para o Cloudinary
        if profile_picture:
            image = create_image(profile_picture, description="Foto de perfil", folder_path="media/profile")
            user.photo_url = image.file  # Atualiza o campo de foto no modelo
            user.save()

        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        data['user_id'] = self.user.id
        data['name'] = self.user.name
        data['email'] = self.user.email
        data['username'] = self.user.username
        data['photo_url'] = self.user.photo_url

        return data
