from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from articles.models import Article, Category

class CategoryAdmin(admin.ModelAdmin):
	fields = ['name', 'parent', ]

admin.site.register(Article)
admin.site.register(Category, CategoryAdmin)


