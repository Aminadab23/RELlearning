from django.urls import path
from . import views 
urlpatterns = [
    path('',views.getCompany.as_view()),
    path('getPackages',views.getPackage.as_view()),
    path('getBooks', views.getBooks.as_view()),
    path('getCourse', views.getCourse.as_view()),
    path('CreatePackage', views.CreatePackage.as_view()),
    path('CreateCourse', views.CreateCourse.as_view()),
    path('CreateBooks', views.CreateBooks.as_view()),
    path('CreateCompany', views.CreatePackage.as_view()),

]
