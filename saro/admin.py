from itertools import product
from pyexpat import model
from django.contrib import admin
from .models import Contact
from products.models import Jenerator
@admin.register(Jenerator)
class JeneratorAdmin(admin.ModelAdmin):
    list_display=['engine','jenModel']
    search_fields =['engine']
    list_filter = ['engine']
    
    class Meta:
        model = Jenerator
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    
    class Meta:
        model=Contact
