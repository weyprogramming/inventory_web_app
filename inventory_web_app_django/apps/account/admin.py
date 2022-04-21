from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Account

class AccountAdmin(UserAdmin):
    list_display = ('email', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email',)
    readonly_fields = ('id', 'date_joined', 'last_login')

    ordering = ('email',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ((None, {'fields': ('email', 'first_name', 'last_name', 'department', 'is_staff', 'is_admin', 'is_superuser')}),)
    add_fieldsets = ((None, {'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'department')}),)


admin.site.register(Account, AccountAdmin)    
