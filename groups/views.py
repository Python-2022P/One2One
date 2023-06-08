from django.http import HttpRequest, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Group
from users.models import User, Contact
from users.views import to_dict
import json


def to_dict_group(group):
    return {
        "id": group.id,
        "name": group.name,
        "students": [to_dict(student) for student in group.students.all()]
    }


def get_groups(request):
    if request.method == "GET":
        groups = Group.objects.all()
        group_list = [to_dict_group(group) for group in groups]
        return JsonResponse(group_list, safe=False)
    
def get_group_id(request:HttpRequest,id) -> JsonResponse:
    if request.method == "GET":
        group = Group.objects.get(id = id)
        return JsonResponse(to_dict_group(group))
    
    elif request.method == "PUT":
        try:
            group = Group.objects.get(id = id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})
        
        data_json = request.body.decode()
        data = json.loads(data_json)

        if data.get('name'):
            group.name = data['name']
        group.save()

        return JsonResponse(to_dict(group))
    
    elif request.method == "DELETE":
        
        group.delete()

        return JsonResponse({'status': 'ok'})
  
