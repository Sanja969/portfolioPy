from rest_framework import generics
from .models import Quote
from .serializers import QuoteSerializer

class Quotes(generics.ListAPIView):
  queryset = Quote.objects.all() 
  serializer_class = QuoteSerializer

class Quote(generics.RetrieveAPIView):
  queryset = Quote.objects.all() 
  serializer_class = QuoteSerializer
