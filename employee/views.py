from django.shortcuts import render, redirect
from employee.models import Employee
from employee.forms import EmployeeListForm, EmployeeForm
from django.db.models import Q
from warsztat.views import home
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.
@login_required
@permission_required("employee.view_employee")
def employee_list(request):
    form=EmployeeListForm(request.POST)
    filter_=Q()
    if form.is_valid():
        if form.cleaned_data["fraze"]:
            filter_ &=Q(Q(first_name__icontains=form.cleaned_data["fraze"])
                        |Q(last_name__icontains=form.cleaned_data["fraze"]))
        if form.cleaned_data["position"]:
            filter_ &= Q(position=form.cleaned_data["position"])
        if form.cleaned_data["status"]:
            filter_ &= Q(status=form.cleaned_data["status"])
    employees=Employee.objects.filter(filter_)
    return render(request=request,        
                    template_name="employee/list.html",
                    context={"employees":employees, "form":form})

@login_required
@permission_required("employee.view_employee")
def employee_details(request,pk):
    employee=Employee.objects.filter(id=pk).first()
    return render(request=request,
                    template_name="employee/details.html",
                    context={"employee":employee})
    

@login_required
@permission_required("employee.add_employee")
def employee_create(request):
    if request.method=="POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("employee-list")
            #employee = Employee.objects.create(
                #first_name = form.cleaned_data["first_name"],
                #last_name = form.cleaned_data["last_name"],
                #birth_date = form.cleaned_data["birth_date"],
                #description = form.cleaned_data["description"],
                #image = form.cleaned_data["image"],)
            #employee = Employee(
            #    first_name = form.cleaned_data["first_name"],
            #    last_name = form.cleaned_data["last_name"],
            #    birth_date = form.cleaned_data["birth_date"],
            #    description = form.cleaned_data["description"],
            #    image = form.cleaned_data["image"],)
            #employee.save()
        
    else:
        form = EmployeeForm()
    return render(request=request,
                    template_name="employee/update.html",
                    context={"form":form})
    
@login_required
@permission_required("employee.change_employee")    
def employee_update(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method=="POST":
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("employee-list")
    else:
        form = EmployeeForm(instance=employee)
    return render(request=request,
                    template_name="employee/update.html",
                    context={"form":form})
    
@login_required
@permission_required("employee.delete_employee")    
def employee_delete(request,pk):
    employee = Employee.objects.get(id=pk)
    employee.delete()
    return redirect("employee-list")
    