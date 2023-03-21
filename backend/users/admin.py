from django.contrib import admin
from .models import CustomUser, Passion, SexualOrientation
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email','gender', 'city', 'state', 'country', 'pincode', 'is_verified']


admin.site.register(Passion)
admin.site.register(SexualOrientation)
admin.site.register(CustomUser, CustomUserAdmin)