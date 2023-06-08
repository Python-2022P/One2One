from django.urls import path
from .views import (
    get_groups,
    get_group_id,
)
                     
urlpatterns = [
    path('', get_groups),
    path('<int:id>',get_group_id),
    
]
