import datetime
from django.db import models
from administrators.models import Course, Package

from users.models import User

# Create your models here.
class Submission(models.Model):
    assignment = models.ForeignKey("teachers.Assignment",  on_delete=models.CASCADE)
    student= models.ForeignKey("users.User", on_delete=models.CASCADE)
    grades= models.CharField(max_length=5)
    

    
    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} {self.assignment.title.lesson_title}"


class Cart(models.Model):
    user= models.ForeignKey(to=User,on_delete=models.CASCADE)
    course= models.ForeignKey(to=Course,on_delete=models.CASCADE)
    startdate= models.DateField(auto_now_add=True)
    endDate=  models.DateField()

    
    def __str__(self):
        return f'{self.user}-{self.course}'
    
class Subscription(models.Model):
    user= models.ForeignKey(to=User,on_delete=models.CASCADE)
    package= models.ForeignKey(to=Package,on_delete=models.CASCADE)
    startDate= models.DateField(auto_now_add=True)
    endDate = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.endDate:
            self.endDate = datetime.timezone.now() + datetime.timedelta(days=365)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.package.package_type