from django import forms

from rent.models import Property, Owner


class CreatePropertyForm(forms.ModelForm):

    owner = forms.ModelChoiceField(
        queryset=Owner.objects.all(),
        widget=forms.RadioSelect,
    )

    description = forms.CharField(
        widget =forms.Textarea,
    )


    class Meta:
        model = Property
        fields = [
            'owner', 'address', 'city', 'property_type', 'description',
            'price', 'rent_length', 'vacant'
        ]
