from django.urls import path
from .views import RarePlantListView, RarePlantDetailView

urlpatterns = [
    path('', RarePlantListView.as_view(), name='rareplant-list'),
    path('rareplant/<int:id>/', RarePlantDetailView.as_view(), name='rareplant-detail'),
]



