from rest_framework import viewsets

from rent.models import Property

from rent.api.serializers import PropertySerializer


# http://localhost:8000/api/properties/?format=json
class PropertyViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    API endpoint for listing properties.
    '''
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
