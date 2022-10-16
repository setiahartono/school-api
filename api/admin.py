from django.contrib import admin
from api.models import School


# Register your models here.
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    pass
