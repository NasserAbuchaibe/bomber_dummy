from django.db import models
from django import forms

# Create your models here.

# model student
class Student(models.Model):
    name = models.CharField(max_length=60)
    score_project1 = models.DecimalField(max_digits=4, decimal_places=2)
    score_project2 = models.DecimalField(max_digits=4, decimal_places=2)
    parent = models.ForeignKey('Parent', on_delete=models.CASCADE, default=None)


    def __str__(self):
        return self.name


# model parent.
class Parent(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    user_name = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name

