from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.CreateUser.as_view()),
    path('exercise/', views.LowerList.as_view(), name='exercise_read'),
   
]
