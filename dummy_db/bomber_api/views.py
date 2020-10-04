from rest_framework import viewsets
from .serializers import ParentSerializer, StudentSerializer
from .models import Parent, Student

# Create your views here.

# viewsets for Parent
class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.filter(password=12345)
    serializer_class = ParentSerializer
    
# viewsets for Student
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.filter(parent_id=13)
    serializer_class = StudentSerializer
