from django import forms
from django.forms.widgets import TextInput
from pricing.models import Pricing

class PricingListForm(forms.Form):
    fraze=forms.CharField(required=False,
                           label="",
                           help_text="",
                           strip=True,
                           empty_value="",
                           max_length=256,
                          widget=TextInput(attrs={"placeholder":"wyszukaj","style":"width:250px"}))
    vehicle= forms.ChoiceField(choices=[("","---"),("Chopper","Chopper"),
                                        ("Motocykl","Motocykl"),
                                        ("Samochód Osobowy","Samochód Osobowy"),
                                        ("Samochód Ciężarowy","Samochód Ciężarowy")],
                                required=False, label="Rodzaj pojazdu")
    

class PricingForm(forms.ModelForm):
    class Meta:
        model = Pricing
        fields = ["service_name",
                  "service_number",
                  "vehicle",
                  "price",
                  "description",
                  "image"]
        

class PricingCustom(forms.ModelForm):
    class Meta:
        model = Pricing
        fields = ["price",]
        

