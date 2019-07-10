from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone', 'email']
    list_display_links = ['id', 'first_name', 'last_name', 'phone', 'email']
    search_fields = ['id', 'first_name', 'last_name', 'email']

admin.site.register(Contact, ContactAdmin)


