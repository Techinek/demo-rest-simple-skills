from rest_framework import generics

from .models import Student
from .serializers import StudentSerializer

class StudentList(generics.ListCreateAPIView):
    """Class for listing all the students"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    """Class for rendering a single student"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer