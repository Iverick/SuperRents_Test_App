from datetime import date, datetime, timedelta

from django.shortcuts import render
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
    View lists all rented properties.
    '''
    template_name = 'rent/list_rented_properties.html'

    def get_queryset(self):
        qs = Property.objects.get_rented_properties()
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['expires_soon'] = self.check_expiration_date()
        return ctx

    def check_expiration_date(self):
        # counting 30 days from now
        today = date.today()
        expires_soon = today + timedelta(days=30)
        
        for object in self.get_queryset():
            return datetime.date(object.contract.end_date) < expires_soon


'''
# http://localhost:8000/rented-properties/
class ListRentedProperties(TemplateView):

    View lists all rented properties.

    template_name = 'rent/list_rented_properties.html'
    properties = Property.objects.get_rented_properties()

    for property_ in properties:
        property_['expires_soon'] = self.check_expiration_date()

    def get_context_data(self, **kwargs):
        context = ({
            'property_': property_
        })
        return context

    def check_expiration_date(self):
        # counting 30 days from now
        today = date.today()
        expires_soon = today + timedelta(days=30)
        
        if datetime.date(property_.contract.end_date) < expires_soon:
            return True
        return False
'''
