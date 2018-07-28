from rest_framework import serializers

from rent.models import Property


class PropertySerializer(serializers.ModelSerializer):

	class Meta:
		model = Property
		fields = (
			'id', 'owner', 'address', 'city', 'property_type', 'price',
			'rent_length', 'vacant'
		)
