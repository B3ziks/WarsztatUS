from django.shortcuts import render, redirect
from pricing.models import Pricing
from pricing.forms import PricingListForm, PricingForm, PricingCustom
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from django.core import serializers

# Create your views here.

def pricing_list(request):
    form=PricingListForm(request.POST)
    filter_=Q()
    if form.is_valid():
        if form.cleaned_data["fraze"]:
            filter_ &=Q(Q(service_name__icontains=form.cleaned_data["fraze"])
                        |Q(service_number__icontains=form.cleaned_data["fraze"])
                        |Q(description__icontains=form.cleaned_data["fraze"]))
        if form.cleaned_data["vehicle"]:
            filter_ &= Q(vehicle=form.cleaned_data["vehicle"])
    pricings=Pricing.objects.filter(filter_)
    return render(request=request,        
                    template_name="pricing/list.html",
                    context={"pricings":pricings, "form":form})


def pricing_details(request,pk):
    pricing=Pricing.objects.filter(id=pk).first()
    return render(request=request,
                    template_name="pricing/details.html",
                    context={"pricing":pricing})
    
@login_required
@permission_required("pricing.add_pricing")
def pricing_create(request):
    if request.method=="POST":
        form = PricingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("pricing-list")
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
        form = PricingForm()
    return render(request=request,
                    template_name="pricing/create.html",
                    context={"form":form})
    
@login_required
@permission_required("pricing.change_pricing")    
def pricing_update(request, pk):
    employee = Pricing.objects.get(id=pk)
    if request.method=="POST":
        form = PricingForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("pricing-list")
    else:
        form = PricingForm(instance=employee)
    return render(request=request,
                    template_name="pricing/update.html",
                    context={"form":form})
    
@login_required
@permission_required("pricing.delete_pricing")      
def pricing_delete(request,pk):
    pricing = Pricing.objects.get(id=pk)
    pricing.delete()
    return redirect("pricing-list")
    
    

    
def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['data'] = [
            {
                'service_number': obj.service_number,
                'price': obj.price,
                'vehicle': obj.vehicle,
            }
            for obj in Pricing.objects.all()
        ]

        return context
    
    
    
def personalize(request):
    form=PricingCustom(request.POST)
    filter_=Q()
    pricings=Pricing.objects.filter(filter_)
    return render(request=request,        
                    template_name="pricing/personalize.html",
                    context={"pricings":pricings, "form":form})


def summary(request):
    return render(request=request,
                    template_name="pricing/summary.html")

