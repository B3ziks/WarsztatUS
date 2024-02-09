from django.urls import path
from employee.views import employee_list
from employee.views import employee_details
from employee.views import employee_create
from employee.views import employee_update
from employee.views import employee_delete
from warsztat.views import home

urlpatterns = [
    path("list/", employee_list, name="employee-list"),
    path("details/<int:pk>/", employee_details, name="employee-details"),
    path("create/", employee_create, name="employee-create"),
    path("update/<int:pk>/", employee_update, name="employee-update"),
    path("delete/<int:pk>/", employee_delete, name="employee-delete"),
]