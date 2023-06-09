from django.db import models
from users.models import User

# Create your models here.


class Group(models.Model):
    
    name = models.CharField(max_length=255)
    students = models.ManyToManyField(User)
    
    def __str__(self) -> str:
        return self.name
    