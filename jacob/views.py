from rest_framework import generics, permissions
from .models import Exercise
from django.contrib.auth import get_user_model, authenticate, logout, login
from .serializers import UserSerializer, ExerciseSerializer, LowerSerializer

class CreateUser(generics.CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class ExerciseList(generics.ListCreateAPIView):
  serializer_class = ExerciseSerializer
  queryset = Exercise.objects.all()
  permission_classes = [permissions.AllowAny]


class LowerList(generics.ListAPIView):
    queryset = Exercise.objects.all()
    serializer_class = LowerSerializer


