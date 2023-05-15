from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Exercise, Program

UserModel = User

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    first_name = serializers.CharField(write_only=True, required=True)
    last_name = serializers.CharField(write_only=True, required=True)
    email = serializers.CharField(write_only=True, required=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
        )

        return user

    class Meta:
        model = UserModel
        fields = ('id', 'username', "password", 'first_name', 'last_name', 'email')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['username'] = user.username
        return token

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class UserForProgramSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'email')

class ProgramSerializer(serializers.ModelSerializer):
    user = UserForProgramSerializer()
    exercise = serializers.SlugRelatedField(many=True, queryset=Exercise.objects.all(), slug_field='name')

    def create (self, validated_data):
        exercise = {}
        user_data = validated_data.pop('user')
        exercise_data= validated_data.pop('exercise')
        user_id = self.context.get('user_id')
        user = User.objects.get(id=user_id)

        exercise_serializer = ExerciseSerializer(data=exercise_data)
        exercise_serializer.is_valid(raise_exception=True)
        exercises = exercise_serializer.save()

        for exercise in exercises:
            print(exercise)

        program = Program.objects.create( 
            user=user, 
            **validated_data)
        
        return program

    class Meta:
        model = Program
        fields = '__all__'

