from django.contrib import admin
from .models import Comic, Reading, Genre

# Register your models here.
admin.site.register(Comic)
admin.site.register(Reading)
admin.site.register(Genre)