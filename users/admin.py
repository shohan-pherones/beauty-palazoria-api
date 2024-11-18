from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address', 'image')
    search_fields = ('user__username', 'phone_number', 'address')
    list_filter = ('user__is_active',)
