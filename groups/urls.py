from django.urls import path
from .views import (
    get_groups,
    get_group_id,
)
                     
urlpatterns = [
   
    path('<int:id>',get_group_id),
    # path('', get_groups),
]
