from rest_framework import serializers

from rent.models import Property


class PropertySerializer(serializers.ModelSerializer):

    property_type_display = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = (
            'id', 'owner', 'address', 'city', 'price', 'property_type',
            'property_type_display', 'rent_length', 'vacant'
        )

    def get_property_type_display(self, obj):
        return obj.get_property_type_display()
