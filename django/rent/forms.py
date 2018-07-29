# django imports
from django import forms
from django.contrib.auth import get_user_model
# local imports
from rent.models import Property, Owner


class CreatePropertyForm(forms.ModelForm):
    '''
    Modelform for a Propety model
    '''
    owner = forms.ModelChoiceField(
        queryset=Owner.objects.all(),
        widget=forms.Select,
    )
    description = forms.CharField(
        widget=forms.Textarea,
    )

    class Meta:
        model = Property
        fields = [
            'owner', 'address', 'city', 'property_type', 'description',
            'price', 'rent_length', 'vacant'
        ]
