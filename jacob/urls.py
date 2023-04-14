from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.CreateUser.as_view()),
    path('exercise/', views.ExerciseList.as_view(), name='exercise_read'),
    path('exercise/<str:category>/', views.ExerciseListByCategory.as_view(), name='exercise_read_by_category'),
    path('exercise/<str:category>/<str:bodygroup>/', views.ExerciseListByCategoryAndBodyGroup.as_view(), name='exercise_read_by_category_and_group'),
    path('exercise/<str:category>/<str:bodygroup>/<str:muscle>', views.ExerciseListByCategoryAndBodyGroupAndMuscle.as_view(), name='exercise_read_by_category_and_group_and_muscle'),
    path('program/<str:username>/', views.ProgramList.as_view(), name='program_read'),
    path('program/<str:username>/<int:day>', views.ProgramDetail.as_view(), name='program_detail'),   
]
