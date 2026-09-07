from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class UserModelAdmin(UserAdmin):
    # model = User
    list_display = ['id', 'email', 'is_active', 'is_staff']
    search_fields = ['email', 'full_name']
    ordering = ['email']
    fieldsets = (
        ('Credenatils',{'fields': ('email', 'password')}),
        ('Personal Information',{'fields': ('full_name', 'phone_number')}),
        ('Permissions',{'fields': ('is_active','is_staff','is_superuser','groups','user_permissions')}),
    )
    add_fieldsets = (
        ('Create New User',{'classes': ('wide',),'fields':('email', 'password1','password2')}),
    )



admin.site.register(User, UserModelAdmin)
