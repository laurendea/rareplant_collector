from rest_framework import serializers
from .models import RarePlant

class RarePlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = RarePlant
        fields = '__all__'

