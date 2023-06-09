from django.urls import path
from .views import *

urlpatterns = [
    path("",get_all_group),
    path("<int: group_id>", get_by_group_id),
    path("<int: gruop_id>/students", get_students_by_group_id),
    path("/<int: groups_id>/add/<int :student_id>", add_student)
]
