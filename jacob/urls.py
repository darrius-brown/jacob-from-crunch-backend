from django.urls import path
from . import views
from .views import LoginView

urlpatterns = [
    path('signup/', views.CreateUser.as_view()),
    path('login/', LoginView.as_view(), name='login'),
    path('create/exercise/', views.CreateExercise.as_view(), name='exercise_create'),
    path('create/program/<int:user_id>/<int:program>/', views.CreateProgram.as_view(), name='exercise_create'),
    path('exercise/', views.ExerciseList.as_view(), name='exercise_read'),
    path('exercise/<str:category>/', views.ExerciseListByCategory.as_view(), name='exercise_read_by_category'),
    path('exercise/<str:category>/<str:bodygroup>/', views.ExerciseListByCategoryAndBodyGroup.as_view(), name='exercise_read_by_category_and_group'),
    # path('exercise/<str:category>/<str:muscle>/', views.ExerciseListByCategoryAndMuscle.as_view(), name='exercise_read_by_category_and_muscle'),
    path('exercise/<str:category>/<str:bodygroup>/<str:muscle>/', views.ExerciseListByCategoryAndBodyGroupAndMuscle.as_view(), name='exercise_read_by_category_and_group_and_muscle'),
    path('program/<str:username>/', views.ProgramList.as_view(), name='program_read'),
    path('program/<str:username>/<int:pk>/', views.ProgramDetail.as_view(), name='program_detail'),   
]
