from rest_framework import viewsets, permissions

from server.permissions import IsSuperUser
from .models import Video
from .serializers import VideoSerializer


class VideoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsSuperUser]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
