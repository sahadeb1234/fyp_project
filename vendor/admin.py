from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import PreRegistration, Vendor

@admin.register(PreRegistration)
class PreRegistrationAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name']


admin.site.register(Vendor)


