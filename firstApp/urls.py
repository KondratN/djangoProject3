from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='firstApp-home'),
    path('users/', views.users, name='firstApp-users'),
    path('tasks/', views.tasks, name='firstApp-tasks'),
    path('reg_user/', views.reg_user, name='firstApp-reguser'),
    path('reg_task/', views.reg_task, name='firstApp-regtask'),
    path('users/<int:id>/', views.get_user_id, name='firstApp-get_user_id'),
    path('tasks/<int:id>/', views.get_task_id, name='firstApp-get_task_id'),
]
