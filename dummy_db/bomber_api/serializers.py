from rest_framework import serializers
from .models import Parent, Student
# Convert the querysets of the models in JSON
# to serve them in the REST API

class ParentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parent
        fields = ('name', 'email')

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'score_project1', 'score_project2', 'parent')