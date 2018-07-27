from django.db import models


class Owner(models.Model):

    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140)
    born = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


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
        null=True
    )
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    property_type = models.IntegerField(choices=PROPRETY_TYPE, default=HOUSING)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('price',)

    def __str__(self):
        return self.address + ' ' + self.city


class RentalAgreement(models.Model):


class RentalPayment(models.Model):
