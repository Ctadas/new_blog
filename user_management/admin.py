from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user_management.models import UserManagement
from django.contrib.auth.forms import ReadOnlyPasswordHashField
# Register your models here.	

class UserManagementAdmin(UserAdmin):
	fieldsets = (
		(None, {'fields': ('username', 'password','head_portrait')}), 
		('个人信息', {'fields': ('first_name', 'last_name', 'email')}), 
		('权限', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}), 
		('重要日期', {'fields': ('last_login', 'date_joined')})
	)



admin.site.register(UserManagement, UserManagementAdmin)