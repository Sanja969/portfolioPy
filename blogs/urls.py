from django.urls import path

from .views import Blogs, Blog

urlpatterns = [
  path('blogs/<int:pk>/', Blog.as_view()),
  path('blogs/', Blogs.as_view()),
]