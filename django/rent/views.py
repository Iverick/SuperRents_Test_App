from datetime import date, datetime, timedelta

from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from rent.forms import CreatePropertyForm
from rent.models import Property


# http://localhost:8000/home/
def get_homepage(request):
    return render(request, 'rent/homepage.html')


# http://localhost:8000/add-property/
class AddProperty(CreateView):
    
    form_class = CreatePropertyForm
    template_name = 'rent/add_property.html'

    def get_success_url(self):
        return reverse('rent:homepage')


# http://localhost:8000/vacant-properties/
class ListVacantProperties(ListView):
    '''
    View lists all vacant Properties
    '''
    template_name = 'rent/list_vacant_properties.html'

    def get_queryset(self):
        qs = Property.objects.get_vacant_properties()
        return qs


# http://localhost:8000/rented-properties/
def list_rented_properties(request):
    '''
    View lists all rented properties.
    '''
    properties = Property.objects.get_rented_properties()
    # counting 30 days from today for an expires_soon context property.
    # will be used in a template later.
    today = date.today()
    expires_soon = today + timedelta(days=30)
    context = {
        'properties': properties,
        'expires_soon': expires_soon
    }
    # print(context)
    return render(request, 'rent/list_rented_properties.html', context)
