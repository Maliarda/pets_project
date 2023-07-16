from django.contrib import admin
from .models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'kind', 'owner')
    list_filter = ('kind', 'owner')
    search_fields = ('name', 'owner__username')
