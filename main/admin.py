from django.contrib import admin

from .models import Todo,Profile
# Register your models here.
admin.site.register(Todo)
admin.site.register(Profile)