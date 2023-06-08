from django.urls import path

from .views import Articles, Article

urlpatterns = [
  path('articles/<int:pk>/', Article.as_view()),
  path('articles/', Articles.as_view()),
]