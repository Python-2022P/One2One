from django.http import HttpRequest, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
import json

# Create your views here.
from .models import User, Contact

def to_dict(users: User)-> dict:
    
    return {
        "id": User.id,
        "first_name": User.first_name,
        "last_name": User.last_name,
        "username": User.username,
        "age": User.age
    }