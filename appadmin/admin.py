from django.contrib import admin

# Register your models here.
from .models import * 

admin.site.register(platform)
admin.site.register(cource)
admin.site.register(tutorial)
admin.site.register(questions)

