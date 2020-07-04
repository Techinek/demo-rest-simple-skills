from rest_framework import generics, mixins

from .models import Student
from .serializers import StudentSerializer

class StudentList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """Class for listing all the students with get and post methods"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class StudentDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    """Class for rendering a single student"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)