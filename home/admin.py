from django.contrib import admin
from .models import Engineer, Review, Certificate


class EngineerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'position']
    list_display_links = ['id', 'first_name', 'last_name', 'position']
    search_fields = ['id', 'first_name', 'last_name', 'position']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name']
    list_display_links = ['id', 'full_name']
    search_fields = ['id', 'full_name']


admin.site.register(Engineer, EngineerAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Certificate)