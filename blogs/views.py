from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer

class Blogs(generics.ListAPIView):
  queryset = Blog.objects.all() 
  serializer_class = BlogSerializer

class Blog(generics.RetrieveAPIView):
  queryset = Blog.objects.all() 
  serializer_class = BlogSerializer