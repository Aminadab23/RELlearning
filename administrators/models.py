from django.db import models

from users.models import User

# Create your models here.
class Company(models.Model):
    name= models.CharField(max_length=100)
    landingDescription= models.TextField()
    goal= models.TextField()
    languagesQuealified= models.TextField()
    mentorsCallMessage= models.TextField()
    exploreEthiopiaText= models.TextField()
    sudentsNumber= models.IntegerField()
    
    def __str__(self):
        return f"{self.name} description"

class Languages(models.Model):
    language= models.CharField(max_length=120)
    
    
    def __str__(self):
        return self.language


class Course(models.Model):
    
    course_title= models.CharField(max_length=60)
    description= models.TextField()
    certification= models.BooleanField(default=False)
    expectedTrainee=models.CharField(max_length=60)
    price= models.CharField(max_length=10)
    duration= models.CharField(max_length=12)
    language= models.ForeignKey(to= Languages,on_delete=models.CASCADE)
    noOfLessons= models.IntegerField()
    noOfQuizes= models.IntegerField()
    teacher= models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_title
class BookType(models.Model):
    type = models.CharField(max_length=200, )
    

    
    def __str__(self):
        return self.type

class Books(models.Model):
    title= models.CharField(max_length=120)
    type= models.ForeignKey(to=BookType,  on_delete=models.CASCADE)
    price= models.CharField(max_length=10)
    numberOfPages= models.IntegerField()
    file= models.FileField( upload_to='books/')
    iconImage= models.ImageField(upload_to='bookIcon/')
    rating= models.CharField(max_length=10)
    uploadDate= models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title 
    
class Package(models.Model):
    package_type= models.CharField(max_length=100)
    pricePerYear= models.CharField(max_length=10)
    generalDescription = models.TextField()
    detailDescription = models.TextField()


    class Meta:
        """Meta definition for Package."""

        verbose_name = 'Package'
        verbose_name_plural = 'Packages'

    def __str__(self):
        return self.package_type
