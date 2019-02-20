from django.contrib import admin
from theme.models import Theme

# Register your models here.
class Theme_Admin(admin.ModelAdmin):
	pass

admin.site.register(Theme, Theme_Admin)