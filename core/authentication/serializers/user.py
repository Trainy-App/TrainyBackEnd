# user.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from core.uploader.utils.create_image import create_image

User = get_user_model()

class UserBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name', 'photo_url')

class UserSerializer(serializers.ModelSerializer):
    profile_picture = serializers.ImageField(write_only=True, required=False)
    perfil = serializers.SerializerMethodField()  # Campo para incluir o objeto relacionado

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'name', 'profile_picture', 'photo_url', 'perfil']
        extra_kwargs = {'password': {'write_only': True}}

    def get_perfil(self, obj):
        # Importa os serializers dentro do método para evitar importações circulares
        if hasattr(obj, 'personal'):
            from core.authentication.serializers.personal import PersonalSerializer
            data = PersonalSerializer(obj.personal).data  # serializa o objeto personal
            data.pop('user', None)
            return data
        elif hasattr(obj, 'athlete'):
            from core.authentication.serializers.athlete import AthleteSerializer
            data = AthleteSerializer(obj.athlete).data  # serializa o objeto athlete
            data.pop('user', None)  # remove a chave 'user' se existir
            return data
        return None

    def create(self, validated_data):
        """Cria um usuário, faz o hash da senha e salva a foto de perfil."""
        profile_picture = validated_data.pop('profile_picture', None)

        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        if profile_picture:
            image = create_image(profile_picture, description="Foto de perfil", folder_path="media/profile")
            user.photo_url = image.file 
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
