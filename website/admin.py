from django.contrib import admin

# Register your models here.
from website.models import Probleme, Probleme_image_xy

admin.site.register(Probleme)
admin.site.register(Probleme_image_xy)
