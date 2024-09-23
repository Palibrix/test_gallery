from django.urls import path
from .views import AntennaListView, AntennaCreateView, CameraListView, AntennaUpdateView

urlpatterns = [
    path('antennas/list', AntennaListView.as_view(), name='list'),
    path('antennas/create', AntennaCreateView.as_view(), name='create_antenna'),
    path('antennas/<int:pk>/update', AntennaUpdateView.as_view(), name='update_antenna'),
    path('cameras/', CameraListView.as_view(), name='camera_list'),
]
