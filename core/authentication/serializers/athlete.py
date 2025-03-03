from rest_framework import serializers
from core.authentication.models import Athlete
from core.authentication.serializers.user import UserSerializer


class AthleteSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Athlete
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        athlete, created = Athlete.objects.update_or_create(user=user, **validated_data)
        return athlete