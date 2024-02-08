from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics, status, permissions
from rest_framework.generics import RetrieveAPIView

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.exceptions import PermissionDenied

from .models import RarePlant, PlantCultivation, PlantOrigin, PlantNurture, MusicPlaylist
from .serializers import RarePlantSerializer, PlantCultivationSerializer,  PlantOriginSerializer, PlantNurtureSerializer, MusicPlaylistSerializer, UserSerializer

# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the rareplant_collector api home route!'}
    return Response(content)
  
class CreateUserView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    user = User.objects.get(username=response.data['username'])
    refresh = RefreshToken.for_user(user)
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': response.data
    })
    
  # User Login
class LoginView(APIView):
  permission_classes = [permissions.AllowAny]

  def post(self, request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
      refresh = RefreshToken.for_user(user)
      return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user': UserSerializer(user).data
      })
    return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# User Verification
class VerifyUserView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    user = User.objects.get(username=request.user)  # Fetch user profile
    refresh = RefreshToken.for_user(request.user)  # Generate new refresh token
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': UserSerializer(user).data
    })

class RarePlantListView(generics.ListCreateAPIView):
    serializer_class = RarePlantSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
      # This ensures we only return cats belonging to the logged-in user
      user = self.request.user
      return RarePlant.objects.filter(user=user)

    def perform_create(self, serializer):
      # This associates the newly created cat with the logged-in user
      serializer.save(user=self.request.user)

class RarePlantDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RarePlantSerializer
    lookup_field = 'id' 
    
    def get_queryset(self):
      user = self.request.user
      return RarePlant.objects.filter(user=user)

    def retrieve(self, request, *args, **kwargs):
      instance = self.get_object()
      serializer = self.get_serializer(instance)

      return Response({
        'rareplant': serializer.data,
    })

    def perform_update(self, serializer):
      rareplant = self.get_object()
      if rareplant.user != self.request.user:
        raise PermissionDenied({"message": "You do not have permission to edit this rare plant."})
      serializer.save()

    def perform_destroy(self, instance):
      if instance.user != self.request.user:
        raise PermissionDenied({"message": "You do not have permission to delete this rare plant."})
      instance.delete() 

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
        This view returns the PlantNurture instances.
        """
        return PlantNurture.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # Assuming 'music_playlists' is the related name for the many-to-many field from PlantNurture to MusicPlaylist
        music_playlists_associated = instance.music_playlists.all()
        music_playlist_serializer = MusicPlaylistSerializer(music_playlists_associated, many=True)

        return Response({
            'plant_nurture': serializer.data,
            'music_playlists_associated': music_playlist_serializer.data
        })


class MusicPlaylistList(generics.ListCreateAPIView):
    queryset = MusicPlaylist.objects.all()
    serializer_class = MusicPlaylistSerializer

class MusicPlaylistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MusicPlaylist.objects.all()
    serializer_class = MusicPlaylistSerializer
    lookup_field = 'id'
    
class AddMusicPlaylistToNurtures(APIView):
    def post(self, request, pk, musicplaylist_id):
        nurture = PlantNurture.objects.get(id=pk)
        music_playlist = MusicPlaylist.objects.get(id=musicplaylist_id)
        
        # Add the music playlist to the nurture
        nurture.music_played.add(music_playlist)
        
        return Response({
            'message': f'Music Playlist {music_playlist.name} successfully added to Nurture {nurture.music_played}.'
        })
        
        