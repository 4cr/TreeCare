from django.contrib import admin
from watering.models import Account, Suburb, WateringSession

admin.site.register(Account)
admin.site.register(Suburb)
admin.site.register(WateringSession)