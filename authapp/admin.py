from django.contrib import admin
from .models import *

# Register your models here.

'''
class TestModelAdmin(admin.ModelAdmin):
    fields = ('description', 'updated', 'created')


class TestModelLogAdmin(admin.ModelAdmin):
    fields = ('description', 'status', 'created')


admin.site.register(TestModel, TestModelAdmin)
admin.site.register(TestModelLog, TestModelLogAdmin)

'''
