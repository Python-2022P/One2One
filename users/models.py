from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name  = models.CharField(max_length=45)
    username   = models.CharField(max_length=45, unique=True)
    age        = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
    

class Contact(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    
    
    def __str__(self):
        return f"{self.user.full_name()} - {self.phone}"


