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

class CreateProgram(generics.CreateAPIView):
    serializer_class = ProgramSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, user_id, program, format=None):
        user_id = self.kwargs['user_id']
        program = self.kwargs['program']
        exercise_ids =  {'1': [[30, 40, 43, 1, 17, 13, 44, 8, 31]],
                         '2': [[30, 40, 43, 1, 17, 13, 4, 34, 45, 44, 6, 38, 8, 31]],
                         '3': [[30, 43, 17, 4, 6, 45, 8], [40, 1, 13, 34, 44, 38, 31]],
                         '4': [[30, 43, 17, 4, 6, 45, 8, 36, 16, 7], [40, 1, 13, 34, 19, 34, 44, 38, 31]],
                         '5': [[30, 43, 17, 4, 6, 45, 8], [40, 1, 13, 34, 44, 38, 31], [30, 43, 17, 4, 6, 45, 8]],
                         '6': [[30, 43, 17, 4, 6, 45, 8, 36, 16, 7], [40, 1, 13, 34, 19, 34, 44, 38, 31], [30, 43, 17, 4, 6, 45, 8, 36, 16, 7]],
                         '7': [[30, 43, 17, 4, 6, 45, 8], [40, 1, 13, 34, 44, 38, 31], [30, 43, 17, 4, 6, 45, 8], [40, 1, 13, 34, 44, 38, 31]],
                         '8': [[30, 43, 17, 4, 6, 45, 8, 36, 16, 7], [40, 1, 13, 34, 19, 34, 44, 38, 31], [30, 43, 17, 4, 6, 45, 8, 36, 16, 7], [40, 1, 13, 34, 19, 34, 44, 38, 31]]
                         }

        program_data = exercise_ids[str(program)]
        if isinstance(program_data, list): 
            for exercises in program_data:
                request.data['exercise'] = exercises
                serializer = ProgramSerializer(data=request.data, context={'user_id': user_id})
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else: 
            request.data['exercise'] = program_data
            serializer = ProgramSerializer(data=request.data, context={'user_id': user_id})
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
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

class ExerciseListByCategoryAndMuscle(generics.ListAPIView):
  serializer_class = ExerciseSerializer
  permission_classes = [permissions.AllowAny]

  def get_queryset(self):
    category = self.kwargs['category']
    muscle = self.kwargs['muscle']
    queryset = Exercise.objects.filter(category=category, muscle=muscle).order_by('id')
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
      queryset = Program.objects.filter(user__username=username).order_by('id')
      return queryset

class ProgramDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = ProgramSerializer
  permission_classes = [permissions.AllowAny]

  def get_queryset(self):
        username = self.kwargs['username']
        queryset = Program.objects.filter(user__username=username)
        return queryset

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)




