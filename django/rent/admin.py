from django.contrib import admin

from rent.models import Owner, Property, RentalContract, RentalPayment


class OwnerAdmin(admin.ModelAdmin):

    search_fields = ['last_name', 'email', 'phone_number']
    ordering = ['last_name',]


class PropertyAdmin(admin.ModelAdmin):

    list_display = [
        'address', 'city', 'property_type', 'price', 'rent_length',
        'vacant', 'owner'
    ]
    list_filter = ['vacant', 'city', 'property_type', 'price', 'rent_length']
    search_fields = ['vacant', 'address', 'city', 'price']
    ordering = [
        'city', 'property_type', 'price', 'vacant', 'address', 'rent_length'
    ]


class RentalContractAdmin(admin.ModelAdmin):

    list_display = [
        'tenant_first_name', 'tenant_last_name', 'start_date', 'end_date',
        'property_id'
    ]
    list_filter = ['end_date']
    search_fields = ['end_date', 'tenant_last_name']
    ordering = ['end_date', 'property_id', 'tenant_last_name']


class RentalPaymentAdmin(admin.ModelAdmin):

    list_display = ['contract_id', 'payment_date' ,'account_balance']
    list_filter = ['payment_date']
    search_fields = ['payment_date']
    ordering = ['payment_date']


admin.site.register(Owner, OwnerAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(RentalContract, RentalContractAdmin)
admin.site.register(RentalPayment, RentalPaymentAdmin)
