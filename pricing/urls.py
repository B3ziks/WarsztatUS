from django.urls import path
from pricing.views import pricing_list, pricing_details, pricing_create,pricing_update, pricing_delete, personalize, summary
from warsztat.views import confirmemail
urlpatterns = [
    path("list/", pricing_list, name="pricing-list"),
    path("details/<int:pk>/", pricing_details, name="pricing-details"),
    path("create/", pricing_create, name="pricing-create"),
    path("update/<int:pk>/", pricing_update, name="pricing-update"),
    path("delete/<int:pk>/", pricing_delete, name="pricing-delete"),
    path("personalize/", personalize, name="personalize"),
    path("summary/", summary, name="summary"),
    path("confirm/", confirmemail, name="confirm"),
]