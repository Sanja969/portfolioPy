from django.urls import path

from .views import Quotes, Quote

urlpatterns = [
  path('quotes/<int:pk>/', Quote.as_view()),
  path('quotes/', Quotes.as_view()),
]