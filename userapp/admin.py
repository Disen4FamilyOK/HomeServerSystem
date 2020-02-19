from django.contrib import admin

# Register your models here.
from .models import TAppuser


class UserAdmin(admin.ModelAdmin):
    list_display=['user_id', 'name', 'phone']
    fields = ['name', 'phone']


admin.site.register(TAppuser, UserAdmin)
