from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from server.api.serializers import UserSerializer, GroupSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Marker

@api_view(['POST', 'GET', 'DELETE'])
def handle_markers_request(request, pk=None):
    if request.method == 'POST':
        create_marker(request)

    elif request.method == 'DELETE':
        delete_marker(pk)

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

def get_markers():
    return Response([{
            'id': m.id, 
            'latitude': m.latitude, 
            'longitude': m.longitude, 
            'altitude': m.altitude
        } for m in Marker.objects.all()
    ])

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