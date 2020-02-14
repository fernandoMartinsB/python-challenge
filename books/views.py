from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer