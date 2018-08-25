from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

SHORT_TEXT_LEN = 500

class Keywords(models.Model):
	name = models.CharField(max_length = 50, unique = True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Ключеві слова'
		verbose_name_plural = 'Ключеві слова'

class News(models.Model):
	title = models.CharField(max_length = 200)
	descriptions = RichTextUploadingField()
	date = models.DateTimeField(auto_now = True)
	image = models.ImageField(upload_to = 'news_image', blank = True, null = True)
	likes = models.IntegerField()
	keywords = models.ManyToManyField(Keywords, related_name = 'keywords', related_query_name = 'keyword')

	def __str__(self):
		return self.title

	def get_short_text(self):
		if len(self.descriptions) > SHORT_TEXT_LEN:
			return self.descriptions[:SHORT_TEXT_LEN]
		else:
			return self.descriptions

	class Meta:
		verbose_name = 'Новини'
		verbose_name_plural = 'Новини'