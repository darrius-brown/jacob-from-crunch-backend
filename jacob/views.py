from rest_framework import generics, permissions
from .models import Exercise, Program
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model, authenticate, logout, login
from .serializers import UserSerializer, ExerciseSerializer, ProgramSerializer

class CreateUser(generics.CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class ExerciseList(generics.ListAPIView):
  serializer_class = ExerciseSerializer
  queryset = Exercise.objects.all().order_by('id')
  permission_classes = [permissions.AllowAny]

class CreateExercise(generics.CreateAPIView):
   serializer_class = ExerciseSerializer
   permission_classes = [permissions.AllowAny]

class CreateProgram(generics.CreateAPIView):
   serializer_class = ProgramSerializer
   permission_classes = [permissions.AllowAny]

   def post(self, request, user_id, format=None):
        user_id = self.kwargs['user_id']
        serializer = ProgramSerializer(data=request.data, context={'user_id': user_id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExerciseListByCategory(generics.ListAPIView):
  serializer_class = ExerciseSerializer
  permission_classes = [permissions.AllowAny]

  def get_queryset(self):
    category = self.kwargs['category']
    queryset = Exercise.objects.filter(category=category).order_by('id')
    return queryset

class ExerciseListByCategoryAndBodyGroup(generics.ListAPIView):
  serializer_class = ExerciseSerializer
  permission_classes = [permissions.AllowAny]

  def get_queryset(self):
    category = self.kwargs['category']
    bodygroup = self.kwargs['bodygroup']
    queryset = Exercise.objects.filter(category=category, muscle_joint_group=bodygroup).order_by('id')
    return queryset

class ExerciseListByCategoryAndBodyGroupAndMuscle(generics.ListAPIView):
  serializer_class = ExerciseSerializer
  permission_classes = [permissions.AllowAny]

  def get_queryset(self):
    category = self.kwargs['category']
    bodygroup = self.kwargs['bodygroup']
    muscle = self.kwargs['muscle']
    queryset = Exercise.objects.filter(category=category, muscle_joint_group=bodygroup, muscle=muscle).order_by('id')
    return queryset

class ProgramList(generics.ListAPIView):
  serializer_class = ProgramSerializer
  permission_classes = [permissions.AllowAny]
  def get_queryset(self):
      username = self.kwargs['username']
      queryset = Program.objects.filter(user__username=username).order_by('day')
      return queryset

class ProgramDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = ProgramSerializer
  permission_classes = [permissions.AllowAny]
  lookup_field = 'day'

  def get_queryset(self):
        username = self.kwargs['username']
        day = self.kwargs['day']
        queryset = Program.objects.filter(user__username=username, day=day)
        return queryset

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)




