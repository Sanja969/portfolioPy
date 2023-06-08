from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer

class Projects(generics.ListAPIView):
  queryset = Project.objects.all() 
  serializer_class = ProjectSerializer

class Project(generics.RetrieveAPIView):
  queryset = Project.objects.all() 
  serializer_class = ProjectSerializer
