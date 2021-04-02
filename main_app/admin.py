from django.contrib import admin
from .models import Comic, Reading, Genre, Photo

# Register your models here.
admin.site.register(Comic)
admin.site.register(Reading)
admin.site.register(Genre)
admin.site.register(Photo)