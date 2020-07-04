from django.shortcuts import render
from django.http import Http404

from rest_framework import viewsets

from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer