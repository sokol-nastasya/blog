from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
import mptt
from ckeditor_uploader.fields import RichTextUploadingField

SHORT_DESCR = 150

class Category(MPTTModel):
	name = models.CharField(max_length = 150)
	parent = TreeForeignKey('self', null = True, blank = True, related_name = 'children', db_index = True)

	def __str__(self):
		return self.name

	class MPTTMeta:
		order_insertion_by = ['name']

	class Meta:
		verbose_name = 'Категорії'
		verbose_name_plural = 'Категорії'

mptt.register(Category, order_insertion_by = ['name'])

class Article(models.Model):
	title = models.CharField(max_length = 100)
	descriptions = RichTextUploadingField()
	date = models.DateTimeField(auto_now = True)
	category = TreeForeignKey(Category, blank = True, null = True)

	def get_short_text(self):
		if len(self.descriptions) > SHORT_DESCR:
			return self.descriptions[:SHORT_DESCR]
		else:
			return self.descriptions

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Статті'
		verbose_name_plural = 'Статті'

