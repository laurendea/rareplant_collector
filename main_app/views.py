from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics
from .models import RarePlant
from .serializers import RarePlantSerializer

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
