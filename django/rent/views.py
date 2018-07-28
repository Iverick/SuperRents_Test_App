from django.shortcuts import render
from django.views.generic import ListView

from rent.models import Property


# http://localhost:8000/vacant-properties/
class ListVacantProperties(ListView):
    '''
    View lists all vacant Properties
    '''
    template_name = 'rent/list_vacant_properties.html'

    def get_queryset(self):
        qs = Property.objects.get_vacant_properties()
        return qs
