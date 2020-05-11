from rest_framework import serializers
from .models import Book, Author, Publisher

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'nationality']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name', 'cowntry']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer();
    publisher = PublisherSerializer();
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher']


