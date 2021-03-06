from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from server.api.serializers import UserSerializer, GroupSerializer, MarkerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Marker

@api_view(['POST', 'GET', 'DELETE'])
def handle_markers_request(request, pk=None):
    if request.method == 'POST':
        create_marker(request)

    elif request.method == 'DELETE':
        if pk is not None:
            delete_marker(pk)
        else:
            delete_all_markers()

    return get_markers()

def create_marker(request):
    Marker.objects.create(
        latitude=request.data['latitude'],
        longitude=request.data['longitude'],
        altitude=request.data['altitude']
    )

def delete_marker(pk):
    filtered_markers = Marker.objects.filter(pk=pk)

    if filtered_markers.exists():
        filtered_markers.first().delete()

def delete_all_markers():
    for marker in Marker.objects.all():
        delete_marker(marker.pk)

def get_markers():
    return Response([{
            'id': m.id, 
            'latitude': m.latitude, 
            'longitude': m.longitude, 
            'altitude': m.altitude
        } for m in Marker.objects.all()
    ])

class MarkerViewSet(viewsets.ModelViewSet):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer
    permission_classes = [permissions.AllowAny]

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]