from rest_framework import serializers

from core.trainy.models import Plan

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'