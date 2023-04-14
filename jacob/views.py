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
  queryset = Exercise.objects.all().order_by('id')
  permission_classes = [permissions.AllowAny]

class ExerciseListByCategory(generics.ListCreateAPIView):
  serializer_class = ExerciseSerializer
  permission_classes = [permissions.AllowAny]

  def get_queryset(self):
    category = self.kwargs['category']
    queryset = Exercise.objects.filter(category=category).order_by('id')
    return queryset

class ExerciseListByCategoryAndBodyGroup(generics.ListCreateAPIView):
  serializer_class = ExerciseSerializer
  permission_classes = [permissions.AllowAny]

  def get_queryset(self):
    category = self.kwargs['category']
    bodygroup = self.kwargs['bodygroup']
    queryset = Exercise.objects.filter(category=category, muscle_joint_group=bodygroup).order_by('id')
    return queryset

class ExerciseListByCategoryAndBodyGroupAndMuscle(generics.ListCreateAPIView):
  serializer_class = ExerciseSerializer
  permission_classes = [permissions.AllowAny]

  def get_queryset(self):
    category = self.kwargs['category']
    bodygroup = self.kwargs['bodygroup']
    muscle = self.kwargs['muscle']
    queryset = Exercise.objects.filter(category=category, muscle_joint_group=bodygroup, muscle=muscle).order_by('id')
    return queryset

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




