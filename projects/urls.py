from django.urls import path

from .views import Projects, Project

urlpatterns = [
  path('projects/<int:pk>/', Project.as_view()),
  path('projects/', Projects.as_view()),
]