from django.contrib import admin
from .models import List

class ListAdmin(admin.ModelAdmin):
    list_display = ("id", "listname", "user")

admin.site.register(List, ListAdmin)