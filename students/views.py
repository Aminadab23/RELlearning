from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics



class SubmitAssignment(generics.CreateAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
 
