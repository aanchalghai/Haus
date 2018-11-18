from django.contrib import admin
from .models import PersonalInfo,RentListings,PgListings,SellListings


# Register your models here.
admin.site.register(PersonalInfo)
admin.site.register(RentListings)
admin.site.register(PgListings)
admin.site.register(SellListings)
