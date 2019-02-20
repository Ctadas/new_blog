from django.contrib import admin
from article.models import Article_type,Article

# Register your models here.
class Article_type_Admin(admin.ModelAdmin):
	pass

class Article_Admin(admin.ModelAdmin):
	 list_display = ('id', 'title', 'release_time','visits')

	 list_display_links = ('id', 'title')

admin.site.register(Article_type, Article_type_Admin)
admin.site.register(Article, Article_Admin)
