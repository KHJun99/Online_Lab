from django.contrib import admin
from .models import Category, Restaurante, Menu

# Register your models here.
admin.site.register(Category)
admin.site.register(Restaurante)
admin.site.register(Menu)
