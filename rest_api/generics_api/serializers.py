from rest_framework import serializers
from fbv_api.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields=['id', 'name', 'score']