from app.models import *
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response

class RegistrationViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    
class RegistrationShowViewSet(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

class CourseViewSet(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseShowViewSet(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class AddstudentViewSet(generics.CreateAPIView):
    queryset = Addstudent.objects.all()
    serializer_class = AddstudentSerializer

class AddstudentShowViewSet(generics.ListAPIView):
    queryset = Addstudent.objects.all()
    serializer_class = AddstudentSerializer

class RegistrationIdViewSet(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

class RegistrationUpdateViewSet(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

class RegistrationDeleteViewSet(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer