from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, permissions
from rest_framework.response import Response
# Create your views here.

class CreateCourse(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CreateCompany(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
class CreateLanguages(generics.CreateAPIView):
    queryset = Languages.objects.all()
    serializer_class = LanguagesSerializer
class CreateBookType(generics.CreateAPIView):
    queryset = BookType.objects.all()
    serializer_class = BookTypeSerializer
class CreateBooks(generics.CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

class CreatePackage(generics.CreateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
 
class getCourse(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
class getBooks(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
class getPackage(generics.ListAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
class getCompany(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
