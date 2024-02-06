from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics
from rest_framework.generics import RetrieveAPIView

from .models import RarePlant, PlantCultivation, PlantOrigin, PlantNurture, MusicPlaylist
from .serializers import RarePlantSerializer, PlantCultivationSerializer,  PlantOriginSerializer, PlantNurtureSerializer, MusicPlaylistSerializer

# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the rareplant_collector api home route!'}
    return Response(content)

class RarePlantListView(generics.ListCreateAPIView):
    queryset = RarePlant.objects.all()
    serializer_class = RarePlantSerializer

class RarePlantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RarePlant.objects.all()
    serializer_class = RarePlantSerializer
    lookup_field = 'id'  

class PlantCultivationDetailView(RetrieveAPIView):
    serializer_class = PlantCultivationSerializer

    def get_object(self):
      
        rareplant_id = self.kwargs['id']
        return PlantCultivation.objects.get(RarePlant__id=rareplant_id)

class PlantOriginDetailView(RetrieveAPIView):
    serializer_class = PlantOriginSerializer

    def get_object(self):
   
        rareplant_id = self.kwargs['id']
        return PlantOrigin.objects.get(RarePlant__id=rareplant_id)
      
      
class PlantNurtureListCreate(generics.ListCreateAPIView):
    serializer_class = PlantNurtureSerializer

    def get_queryset(self):
        """
        This view returns a list of all the PlantNurture records
        for a specific RarePlant, determined by the rareplant_id in the URL.
        """
        rareplant_id = self.kwargs['rareplant_id']
        return PlantNurture.objects.filter(RarePlant__id=rareplant_id)

    def perform_create(self, serializer):
        """
        Overrides the default perform_create method to ensure that
        the PlantNurture instance is associated with the specific RarePlant.
        """
        rareplant_id = self.kwargs['rareplant_id']
        rareplant = RarePlant.objects.get(id=rareplant_id)
        serializer.save(RarePlant=rareplant)
        
        
class PlantNurtureDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlantNurtureSerializer
    lookup_field = 'id'

    def get_queryset(self):
        """
        This view returns the PlantNurture instance that matches the 
        pk from the URL and is associated with the specified RarePlant.
        """
        rareplant_id = self.kwargs['rareplant_id']
        return PlantNurture.objects.filter(RarePlant__id=rareplant_id)


class MusicPlaylistList(generics.ListCreateAPIView):
    queryset = MusicPlaylist.objects.all()
    serializer_class = MusicPlaylistSerializer

class MusicPlaylistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MusicPlaylist.objects.all()
    serializer_class = MusicPlaylistSerializer
    lookup_field = 'id'