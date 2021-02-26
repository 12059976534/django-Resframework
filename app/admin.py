from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.User)
admin.site.register(models.Kota)
admin.site.register(models.Leveluser)
admin.site.register(models.Comment)