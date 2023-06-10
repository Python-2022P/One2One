from django.http import HttpRequest,JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import User,Contact
import json

def to_dict(user: User) -> dict:
    return {
        'id' : user.pk,
        'first_name' : user.first_name,
        'last_name' : user.last_name,
        'username' : user.username,
        'age' : user.age,
        'created_at' : user.created_at,
        'updated_at' : user.updated_at
    }

def to_contact(contact:Contact) -> dict:
    return {
        'id' : contact.pk,
        'user_id' : contact.user.pk,
        'phone' : contact.phone,
        'address' : contact.address,
        'city' : contact.city
    }


def get_users(request:HttpRequest) -> JsonResponse:
    if request.method == 'GET':

        users = User.objects.all()
        
        results = [to_dict(user) for user in users]

        return JsonResponse(results,safe=False)
    
    elif request.method == 'POST':
        data_json = request.body.decode()
        data = json.loads(data_json)
        
        if not data.get('first_name'):
            return JsonResponse({'status':"first_name yo'q"})
        elif not data.get('last_name'):
            return JsonResponse({'status':'last_name yo\'q'})
        elif not data.get('username'):
            return JsonResponse({'status':'username yo\'q'})
        elif not data.get('age'):
            return JsonResponse({'status':'age yo\'q'})
        
        user = User.objects.create(
            first_name = data['first_name'],
            last_name = data['last_name'],
            username = data['username'],
            age = data['age']
        )

        user.save()

        return JsonResponse(to_dict(user))
    
def get_user_id(request:HttpRequest,id) -> JsonResponse:
    if request.method == "GET":
        user = User.objects.get(id = id)
        return JsonResponse(to_dict(user))
    
    elif request.method == "PUT":
        try:
            user = User.objects.get(id = id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})
        
        data_json = request.body.decode()
        data = json.loads(data_json)

        if data.get('first_name'):
            user.first_name = data['first_name']
        if data.get('last_name'):
            user.last_name = data['last_name']
        if data.get('username'):
            user.last_name = data['username']
        if data.get('age'):
            user.age = data['age']

        user.save()

        return JsonResponse(to_dict(user))
    
    elif request.method == "DELETE":
        try:
            phone = User.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})

        phone.delete()

        return JsonResponse({'status': 'ok'})
    
def contact(request:HttpRequest, id) -> JsonResponse:
    if request.method == 'GET':
        try:
            user = User.objects.get(id = id)
            contact = Contact.objects.get(user = user)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})
        
        contact = Contact.objects.get(id = id)
        return JsonResponse(to_contact(contact))
    
    elif request.method == 'POST':
        data_json = request.body.decode()
        data = json.loads(data_json)

        user = User.objects.get(id = id)

        contact = Contact.objects.create(
            user_id = user,
            phone = data['phone'],
            address = data['address'],
            city = data['city']
        )

        contact.save()

        return JsonResponse(to_contact(contact))

    elif request.method == 'PUT':
        data_json = request.body.decode()
        data = json.loads(data_json)

        try:
            user = User.objects.get(id = id)
            contact = Contact.objects.get(user = user)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})
        

        if data.get('phone'):
            contact.phone = data['phone']
        if data.get('address'):
            contact.address = data['address']
        if data.get('city'):
            contact.city = data['city']

        contact.save()

        return JsonResponse(to_contact(contact))

    elif request.method == 'DELETE':
        try:
            user = User.objects.get(id=id)
            contact = Contact.objects.get(user=user)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})

        contact.delete()

        return JsonResponse({'status': 'ok'})

    
def get_all(request:HttpRequest)->JsonResponse:
    users = User.objects.all()

    results = []
    for user in users:
        user_data = to_dict(user)
        try:
            contact = Contact.objects.get(user = user)
            user_data['contact'] = to_contact(contact)
        except ObjectDoesNotExist:
            user_data['contact'] = None

        results.append(user_data)

    return JsonResponse(results,safe=False)



