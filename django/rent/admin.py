from django.contrib import admin

from rent.models import Owner, Property, RentalContract, RentalPayment


admin.site.register(Owner)
admin.site.register(Property)
admin.site.register(RentalContract)
admin.site.register(RentalPayment)
