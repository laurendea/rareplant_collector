

from rest_framework import serializers
from django.contrib.auth.models import User

from .models import RarePlant, PlantCultivation, PlantOrigin, PlantNurture, MusicPlaylist

class RarePlantSerializer(serializers.ModelSerializer):
    nurtured_for_today = serializers.SerializerMethodField()
    user = serializers.PrimaryKeyRelatedField(read_only=True) 
    
    class Meta:
        model = RarePlant
        fields = '__all__'
        
    def get_nurtured_for_today(self, obj):
        return obj.nurtured_for_today()
    

class PlantCultivationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantCultivation
        fields = '__all__'
        read_only_fields = ('RarePlant',)
        
class PlantOriginSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantOrigin
        fields = '__all__'
        read_only_fields = ('RarePlant',)
        
class MusicPlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicPlaylist
        fields = '__all__'
        read_only_fields = ('RarePlant',)       
        
class PlantNurtureSerializer(serializers.ModelSerializer):
    music_played = MusicPlaylistSerializer(many=True, read_only=True)
    class Meta:
        model = PlantNurture
        fields = '__all__'
        read_only_fields = ('RarePlant',)
        
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Add a password field, make it write-only

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
    
    def create(self, validated_data):
      user = User.objects.create_user(
          username=validated_data['username'],
          email=validated_data['email'],
          password=validated_data['password']  # Ensures the password is hashed correctly
      )
      
      return user