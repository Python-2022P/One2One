from django.db import models
from users.models import User

<<<<<<< HEAD
# Create your models here.


class Group(models.Model):
    
    name = models.CharField(max_length=255)
    students = models.ManyToManyField(User)
    
    def __str__(self) -> str:
        return self.name
    
=======
class Group(models.Model):
    name = models.CharField(max_length=20, unique=True)
    students = models.ManyToManyField(User)

    def __str__(self):
        return self.name
>>>>>>> 8bcb8a02107cde688878cff49505c930f52d9f70
