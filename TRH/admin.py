from django.contrib import admin
from . models import Admission, Resort, Customer, Cottage, Reservation
# from .models import User, Info

admin.site.register(Admission)
admin.site.register(Resort)
admin.site.register(Customer)
admin.site.register(Cottage)
admin.site.register(Reservation)



# admin.site.register(User)
# admin.site.register(Info)
