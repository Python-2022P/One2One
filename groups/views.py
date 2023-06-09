from django.shortcuts import render
from django.http import HttpRequest,JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from json import loads
from .models import Group
from users.models import User
from users.views import to_dict

# Create your views here.

def to_dict_group(group: Group):
    
    return {
        "name": group.name,
        "student": [to_dict(students) for students in group.students]
    }

def get_all_group(request: HttpRequest):
    
    if request.method=="GET":
        group = Group.objects.all()
        data = [to_dict_group(group_index) for group_index in group]
        return to_dict_group(data)
    
    elif request.method=="POST":
        data : dict = loads(request.body.decode())
        if data.keys() in ["name", "students"]:
            if type(data["students"])=="list":
            
                    students = []
                    not_fount_students = []
                    for student_id in data["students"]:
                        try:
                            students.append(User.objects.get(id=student_id))
                        except ObjectDoesNotExist:
                            not_fount_students.append(student_id)
                    if students:
                        return to_dict_group(Group.objects.create(name=data["name"],students=students))
                    else:
                        return JsonResponse({"eror" : "Invalid request"})

def get_by_group_id(request: HttpRequest,group_id):
    
    if request.method=="GET":
        try :
            group=Group.objects.get(id=group_id)
        except ObjectDoesNotExist:
            return JsonResponse({"eror": "Invalid id number"})
        
        return to_dict_group(group)
    
    elif request.method=="POST":
        data : dict = loads(request.body.decode())
        if data.keys() in ["name", "students"]:
            if type(data["students"])=="list":
            
                    students = []
                    not_fount_students = []
                    for student_id in data["students"]:
                        try:
                            students.append(User.objects.get(id=student_id))
                        except ObjectDoesNotExist:
                            not_fount_students.append(student_id)
                    if students:
                        try:
                            groups = Group.objects.get(id=group_id)
                            groups.name=data["name"]
                            groups.students=data["students"]
                            return to_dict_group(groups)
                        except ObjectDoesNotExist:
                            return JsonResponse({"eror" : "Invalid id"})
                    else:
                        return JsonResponse({"eror" : "Invalid request"})
                    
    elif request.method == "DELETE":
        
        try :
            
            group = Group.objects.get(id=group_id)
            data=group
            group.delete()
            return JsonResponse({"status": f'deleted {data.name} group'})
        
        except ObjectDoesNotExist:
            return JsonResponse({"eror" : "Group does not exist"})
        
        
def get_students_by_group_id(request: HttpRequest, group_id):
    
    if request.method=="GET":
        try: 
            return JsonResponse(to_dict_group(Group.objects.get(id=group_id))["students"],safe=False)
        except ObjectDoesNotExist:
            return JsonResponse({"error": "Invalid id"})
        
        
def add_student(request: HttpRequest,group_id,student_id):
    if request.method=="POST":
        try:
            group: Group = Group.objects.get(id = group_id)
        except ObjectDoesNotExist:
            return JsonResponse({"error": "Not found group, this invalid id"})

        try:
            student = User.objects.get(id = student_id)
        except ObjectDoesNotExist:
            return JsonResponse({"error": "Not found Student, this invalid id"})
        group.students.add(student)
        return to_dict(student)
    elif request.method=="DELETE":
        try:
            group: Group = Group.objects.get(id = group_id)
        except ObjectDoesNotExist:
            return JsonResponse({"error": "Not found group, this invalid id"})

        try:
            student = User.objects.get(id = student_id)
        except ObjectDoesNotExist:
            return JsonResponse({"error": "Not found Student, this invalid id"})
        group.students.remove(student)
        return JsonResponse({to_dict(student)})
