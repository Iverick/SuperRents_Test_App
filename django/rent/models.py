from django.db import models


class Owner(models.Model):
    # Would have been nice to make Owner an instance of User model.
    # Avoided that for simplicity sake.
    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140)
    born = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class PropertyManager(models.Manager):

    def get_vacant_properties(self):
        qs = self.get_queryset()
        qs = qs.filter(vacant=True)
        return qs

    def get_rented_properties(self):
        qs = self.get_queryset()
        qs = qs.filter(vacant=False)
        return qs


class Property(models.Model):

    HOUSING = 0
    COMMERCIAL = 1
    PROPRETY_TYPE = (
        (HOUSING, 'Housing'),
        (COMMERCIAL, 'Commercial property'),
    )

    owner = models.ForeignKey(
        Owner,
        related_name='properties',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    address = models.CharField(max_length=70)
    city = models.CharField(max_length=50)
    property_type = models.IntegerField(choices=PROPRETY_TYPE, default=HOUSING)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    vacant = models.BooleanField(default=True)
    objects = PropertyManager()

    class Meta:
        ordering = ('price',)

    def __str__(self):
        return self.address + ' ' + self.city


class RentalContract(models.Model):
    '''
    It's currently possible to add a RentalContract to a vacant property which
        is obviously looks like a stupid idea.
    '''
    property_id = models.OneToOneField(
        Property,
        related_name='contract',
        on_delete=models.CASCADE
    )
    # frankly adding a Tenant model would have been nice
    tenant_first_name = models.CharField(max_length=140)
    tenant_last_name = models.CharField(max_length=140)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=False)

    class Meta:
        ordering = ('end_date',)


'''
class RentalPayment(models.Model):

    contract_id = models.OneToOneField(
        RentalContract,
        related_name='contract',
        on_delete=models.CASCADE
    )
    account_balance = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField()
'''
