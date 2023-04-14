from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.CreateUser.as_view()),
    path('exercise/', views.ExerciseList.as_view(), name='exercise_read'),
    path('<int:username>/<int:pk>/', views.ProgramDetail.as_view(), name='program_detail'),
   
]
