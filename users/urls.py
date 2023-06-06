from django.urls import path
from .views import (
    get_users,
    get_user_id,
    contact,
    get_all
)
                     

urlpatterns = [
    path('', get_users),
    path('<int:id>',get_user_id),
    path('<int:id>/contact/',contact),
    path('get-all',get_all)
]
