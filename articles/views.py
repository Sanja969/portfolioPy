from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer

class Articles(generics.ListAPIView):
  queryset = Article.objects.all() 
  serializer_class = ArticleSerializer

class Article(generics.RetrieveAPIView):
  queryset = Article.objects.all() 
  serializer_class = ArticleSerializer
