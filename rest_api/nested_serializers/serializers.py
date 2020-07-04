from rest_framework import serializers

from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    """Serializer for a Book model"""
    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for an Author model"""
    books = BookSerializer(read_only=True, many=True)
    class Meta:
        model = Author
        fields = '__all__'