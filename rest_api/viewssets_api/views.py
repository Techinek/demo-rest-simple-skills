from rest_framework import viewsets

from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """Class for rendering both single and many students"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer