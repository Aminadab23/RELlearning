from .models import *
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Course
        fields = '__all__'
        

class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Lessons
        fields = '__all__'

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Assignment
        fields = '__all__'       
        