from rest_framework import serializers
from .models import Book, Author, Publisher

class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    publisher = serializers.StringRelatedField()
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher']




class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'nationality']




class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name', 'cowntry']



