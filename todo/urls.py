from django.urls import path
from . import views

urlpatterns = [
    # add task
    path('addTask/', views.addTask, name='addTask'),
    # mark task as done
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    # mark task as undone
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),

    #Edit task
    path('editTask/<int:pk>/', views.editTask, name='editTask'),

    # delete task
    path('deleteTask/<int:pk>/', views.deleteTask, name='deleteTask'),


]