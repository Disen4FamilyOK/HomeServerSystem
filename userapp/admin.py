from django.contrib import admin

# Register your models here.
from .models import TAppuser


class UserAdmin(admin.ModelAdmin):
    def realname(self):
        return self.realname_state

    list_display=['user_id', 'name', 'phone', realname]
    fields = ['name', 'phone', 'has_realname']
    list_per_page = 2

    realname.short_description = '实名状态'


admin.site.register(TAppuser, UserAdmin)
