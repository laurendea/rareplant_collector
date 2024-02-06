from rest_framework import serializers
from .models import RarePlant, PlantCultivation, PlantOrigin, PlantNurture, MusicPlaylist

class RarePlantSerializer(serializers.ModelSerializer):
    nurtured_for_today = serializers.SerializerMethodField()
    
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
        
class PlantNurtureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantNurture
        fields = '__all__'
        read_only_fields = ('RarePlant',)
        
class MusicPlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicPlaylist
        fields = '__all__'
        read_only_fields = ('RarePlant',)