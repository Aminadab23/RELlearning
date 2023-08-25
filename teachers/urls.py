from django.urls import path 
from .import views
urlpatterns = [
    path('createCourse',views.CourseCreate.as_view()),
    path('createLesson',views.LessonCreate.as_view()),
    path('createAssignment',views.AssignmentCreate.as_view()),

]
