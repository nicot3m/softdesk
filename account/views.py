from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User

from .serializers import UserSerializer


# Create your views here.
class AccountViewSet(ModelViewSet):
    """
    Create, view or edit a user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
