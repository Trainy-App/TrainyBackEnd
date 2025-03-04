from rest_framework import serializers
from core.authentication.models import Personal
from core.authentication.serializers.user import UserBasicSerializer


class PersonalSerializer(serializers.ModelSerializer):
    user = UserBasicSerializer()

    class Meta:
        model = Personal
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserBasicSerializer.create(UserBasicSerializer(), validated_data=user_data)
        personal, created = Personal.objects.update_or_create(user=user, **validated_data)
        return personal
    