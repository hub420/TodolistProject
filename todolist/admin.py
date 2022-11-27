#this showup in the admin site
from django.contrib import admin

# significao de  . importando desde el mismo directorio models.py 
from .models import Todolist

# Register your models here.
admin.site.register(Todolist)
