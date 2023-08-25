from django.shortcuts import render
from rest_framework import generics
from teachers.models import *
from teachers.serializers import *

# Create your views here.
class CourseCreate(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonCreate(generics.CreateAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer


class AssignmentCreate(generics.CreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
 
 