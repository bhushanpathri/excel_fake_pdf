from django.db import models


# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    address =models.TextField()
    skill = models.CharField(max_length=64)

    def __str__(self):
        return self.name
    
class EmailModel(models.Model):

    email = models.EmailField()
    def __str__(self):
        return self.email
    

