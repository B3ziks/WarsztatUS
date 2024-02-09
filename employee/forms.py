from django import forms
from django.forms.widgets import TextInput
from employee.models import Employee, Position

class EmployeeListForm(forms.Form):
    fraze=forms.CharField(required=False,
                           label="",
                           help_text="",
                           strip=True,
                           empty_value="",
                           max_length=256,
                          widget=TextInput(attrs={"placeholder":"wyszukaj","style":"width:250px"}))
    position=forms.ModelChoiceField(queryset=Position.objects.all(),required=False,label="Stanowisko")
    status= forms.ChoiceField(
        choices=[("","----"),] + Employee.STATUSES,
        required=False, 
        label="Status")

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["first_name",
                  "last_name",
                  "birth_date",
                  "description",
                  "position",
                  "status",
                  "image"]
        widgets = {"birth_date":TextInput(attrs={"type":"date"})}
        

