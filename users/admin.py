from django.contrib import admin

from .models import UserModel


class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_staff')
    readonly_fields = ('password', 'created', 'modified', 'last_login')


admin.site.register(UserModel, UserModelAdmin)
