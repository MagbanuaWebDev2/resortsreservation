from django.contrib import admin
from . models import Resort, Customer, Reservation, Card, Parking

admin.site.register(Resort)
admin.site.register(Customer)
admin.site.register(Parking)
admin.site.register(Reservation)
admin.site.register(Card)

