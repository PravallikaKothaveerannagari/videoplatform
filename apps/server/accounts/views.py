from django.contrib.auth.models import User
from rest_framework import viewsets, permissions

from server.permissions import IsSuperUser
from .serializers import UserModelSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsSuperUser]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
