from django.contrib import admin
from news.models import News, Keywords

class KeywordsAdmin(admin.ModelAdmin):
	fields = ['name', ]

admin.site.register(News)
admin.site.register(Keywords, KeywordsAdmin)
