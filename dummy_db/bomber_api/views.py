from rest_framework import viewsets
from .serializers import ParentSerializer, StudentSerializer
from .models import Parent, Student

# Create your views here.

# viewsets for Parent
class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all().order_by('name')
    serializer_class = ParentSerializer
    
# viewsets for Student
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('name')
    serializer_class = StudentSerializer
