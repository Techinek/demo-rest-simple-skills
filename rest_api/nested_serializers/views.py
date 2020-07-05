from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions


from .serializers import AuthorSerializer, BookSerializer
from .models import Author, Book


class AuthorPagination(PageNumberPagination):
    """Class that overrides default rest pagination settings in settings.py for Author View"""
    page_size = 1


class BookPagination(PageNumberPagination):
    """Class that overrides default rest pagination settings in settings.py for Book View"""
    page_size = 1


class AuthorListView(generics.ListCreateAPIView):
    """Class for listing all authors"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = AuthorPagination
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Class for rendering one author"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListView(generics.ListCreateAPIView):
    """Class for listing all books"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPagination


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Class for rendering one book"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

