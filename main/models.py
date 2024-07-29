from django.db import models
 

# Create your models here.

class Todo(models.Model):
    task = models.TextField()
    quantity = models.IntegerField(null=True)
    complete = models.BooleanField(default=False)
    
    
class Profile(models.Model):
    img = models.ImageField(upload_to="profile_pic/")
    name = models.TextField()
    number = models.IntegerField(null=True)