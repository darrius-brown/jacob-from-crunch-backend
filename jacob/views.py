from rest_framework import generics, permissions
from .models import Exercise, Program
from rest_framework import status
from random import sample
from rest_framework.response import Response
from django.contrib.auth import get_user_model, authenticate, logout, login
from .serializers import UserSerializer, ExerciseSerializer, ProgramSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class CreateUser(generics.CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username:
           return Response('Username can\'t be blank.')
        user = authenticate(request, username=username, password=password)

        if user is None:
            return Response({'error': 'Invalid username/password'}, status=400)

        refresh = RefreshToken.for_user(user)

        data = {
           'username': user.username,
            'user_id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return Response(data)

class ExerciseList(generics.ListAPIView):
  serializer_class = ExerciseSerializer
  queryset = Exercise.objects.all().order_by('id')
  permission_classes = [permissions.AllowAny]

class CreateExercise(generics.CreateAPIView):
   serializer_class = ExerciseSerializer
   permission_classes = [permissions.AllowAny]

# class CreateProgram(generics.CreateAPIView):
  #  serializer_class = ProgramSerializer
  #  permission_classes = [permissions.AllowAny]

  #  def post(self, request, user_id, format=None):
  #       user_id = self.kwargs['user_id']
  #       serializer = ProgramSerializer(data=request.data, context={'user_id': user_id})
  #       if serializer.is_valid():
  #           serializer.save()
  #           return Response(serializer.data, status=status.HTTP_201_CREATED)
  #       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateProgram(generics.CreateAPIView):
    serializer_class = ProgramSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, user_id, format=None):
        user_id = self.kwargs['user_id']

        # Get six random exercises
        exercises = sample(list(Exercise.objects.filter(category='Lower')), 2)
        exercise_ids = [exercise.id for exercise in exercises]

        # Add exercise ids to request data
        request.data['exercise'] = exercise_ids

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




