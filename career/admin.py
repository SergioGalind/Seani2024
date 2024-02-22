from django.contrib import admin

from .models import Career


class CarrerAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'level']
    list_filter = ['level']

admin.site.register(Career, CarrerAdmin)