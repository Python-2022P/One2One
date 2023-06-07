from django.urls import path
from .views import (
    get_groups,
)
                     
urlpatterns = [
    path('', get_groups),
]