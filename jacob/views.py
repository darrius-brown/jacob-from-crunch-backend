from rest_framework import generics, permissions
from .models import Exercise, Program
from django.contrib.auth import get_user_model, authenticate, logout, login
from .serializers import UserSerializer, ExerciseSerializer, ProgramSerializer

class CreateUser(generics.CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class ExerciseList(generics.ListCreateAPIView):
  serializer_class = ExerciseSerializer
  queryset = Exercise.objects.all()
  permission_classes = [permissions.AllowAny]

class ProgramList(generics.ListCreateAPIView):
  serializer_class = ProgramSerializer
  queryset = Program.objects.all()
  permission_classes = [permissions.AllowAny]

class ProgramDetail(generics.RetrieveUpdateDestroyAPIView):
  
  serializer_class = ProgramSerializer
  permission_classes = [permissions.AllowAny]

  def get_queryset(self):
        username = self.kwargs['username']
        queryset = Program.objects.filter(username=username)
        return queryset

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)



