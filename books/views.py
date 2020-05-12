from rest_framework import viewsets
from .serializers import BookSerializer, AuthorSerializer, PublisherSerializer
from .models import Book, Author, Publisher


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows author to be viewed or edited
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer




class PublisherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows publisher to be viewed or edited
    """
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
