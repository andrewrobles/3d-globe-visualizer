from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from server.api.serializers import UserSerializer, GroupSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Marker

@api_view(['POST', 'GET'])
def handle_markers_request(request):
    if request.method == 'POST':
        Marker.objects.create(
            latitude=request.data['latitude'],
            longitude=request.data['longitude'],
            altitude=request.data['altitude']
        )

    # Return all markers in response
    return Response([{
            'id': m.id, 
            'latitude': m.latitude, 
            'longitude': m.longitude, 
            'altitude': m.altitude
        } for m in Marker.objects.all()
    ])

@api_view(['DELETE'])
def delete_marker(request, pk):
    filtered_markers = Marker.objects.filter(pk=pk)

    if filtered_markers.exists():
        filtered_markers.first().delete()
    
    # Return all markers in response
    return Response([{
            'id': m.id, 
            'latitude': m.latitude, 
            'longitude': m.longitude, 
            'altitude': m.altitude
        } for m in Marker.objects.all()
    ])

@api_view(['GET'])
def helloworld(request):
    return Response({'message': 'Hello World!'})

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