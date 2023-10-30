from app.models import *
from .serializers import RegistrationSerializer
from rest_framework import generics
from rest_framework.response import Response

class RegistrationViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    