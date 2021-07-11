from django.contrib import admin
from .models import Category, Items, NeededMaterial, ParentCategory ,ChildCategory, WorkPlace

# Register your models here.
admin.site.register(ParentCategory)
admin.site.register(Category)
admin.site.register(ChildCategory)
admin.site.register(Items)
admin.site.register(WorkPlace)
admin.site.register(NeededMaterial)