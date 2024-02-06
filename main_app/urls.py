from django.urls import path
from .views import RarePlantListView, RarePlantDetailView, PlantCultivationDetailView, PlantOriginDetailView, PlantNurtureListCreate, PlantNurtureDetailView, MusicPlaylistList, MusicPlaylistDetail

urlpatterns = [
    path('', RarePlantListView.as_view(), name='rareplant-list'),
    path('rareplant/<int:id>/', RarePlantDetailView.as_view(), name='rareplant-detail'),
    path('rareplant/<int:id>/plantcare/', PlantCultivationDetailView.as_view(), name='plantcare-detail'),
    path('rareplant/<int:id>/plantorigin/', PlantOriginDetailView.as_view(), name='plantorigin-detail'),
    path('rareplant/<int:rareplant_id>/nurtures/', PlantNurtureListCreate.as_view(), name='plantnurture-listcreate'),
    path('rareplant/<int:rareplant_id>/nurtures/<int:pk>/', PlantNurtureDetailView.as_view(), name='plantnurture-detail'),
    path('musicplaylist/', MusicPlaylistList.as_view(), name='playlist-list'),
    path('musicplaylist/<int:id>/', MusicPlaylistDetail.as_view(), name='playlist-detail'),
]



