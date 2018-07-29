from datetime import date, datetime, timedelta
# django imports
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView
from django.views.generic.edit import CreateView
# local imports
from rent.forms import CreatePropertyForm
from rent.models import Property


# http://localhost:8000/home/
def get_homepage(request):
    '''
    This is root page
    '''
    return render(request, 'rent/homepage.html')


# http://localhost:8000/add-property/
class AddProperty(CreateView):
    '''
    Creates property object using CreatePropertyForm
    '''
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
class ListRentedProperties(ListView):
    '''
    View lists all rented Properties
    '''
    template_name = 'rent/list_rented_properties.html'

    def get_queryset(self):
        # returns list of properties with vacant=False
        qs = Property.objects.get_rented_properties()
        return qs

    def get_context_data(self, **kwargs):
        # adds custom 30_days context variable
        # will be used in a template for changing markup style
        ctx = super().get_context_data(**kwargs)
        ctx['30_days'] = self.count_30_days_from_now()
        return ctx

    def count_30_days_from_now(self):
        # counts 30 days from current date
        today = date.today()
        return today + timedelta(days=30)
