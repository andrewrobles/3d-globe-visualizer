from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from server.api.serializers import UserSerializer, GroupSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Marker

@api_view(['POST'])
def create_marker(request):
    Marker.objects.create(
        latitude=request.data['latitude'],
        longitude=request.data['longitude'],
        altitude=request.data['altitude']
    )

    markers = []
    for current_marker in Marker.objects.all():
        markers.append({
            'id': current_marker.id,
            'latitude': current_marker.latitude,
            'longitude': current_marker.longitude,
            'altitude': current_marker.altitude
        })

    return Response(markers)

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