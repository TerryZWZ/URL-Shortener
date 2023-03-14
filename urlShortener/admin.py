from django.contrib import admin
from .models import ShortURL

# Adding Admin Page
admin.site.register(ShortURL)