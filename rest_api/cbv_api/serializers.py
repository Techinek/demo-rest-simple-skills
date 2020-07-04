from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    """Serializer for a Student model"""
    class Meta:
        model = Student
        fields=['id', 'name', 'score']