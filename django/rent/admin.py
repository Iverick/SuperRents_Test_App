from django.contrib import admin

from rent.models import Owner, Property, RentalContract


admin.site.register(Owner)
admin.site.register(Property)
admin.site.register(RentalContract)
