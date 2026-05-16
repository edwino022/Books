from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# List all books or create a new one
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Retrieve or delete a specific book (optional)
class BookDetailView(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
