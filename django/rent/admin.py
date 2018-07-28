from django.contrib import admin

from rent.models import Owner, Property, RentalContract, RentalPayment


class OwnerAdmin(admin.ModelAdmin):
    search_fields = ('last_name', 'email', 'phone_number')
    ordering = ('last_name',)


class PropertyAdmin(admin.ModelAdmin):
    search_fields = ('address', 'city', 'price')
    ordering = ('address',)

admin.site.register(Owner, OwnerAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(RentalContract)
admin.site.register(RentalPayment)
