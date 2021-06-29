from django.contrib import admin
from .models import Category, Items, ParentCategory

# Register your models here.
admin.site.register(ParentCategory)
admin.site.register(Items)
admin.site.register(Category)