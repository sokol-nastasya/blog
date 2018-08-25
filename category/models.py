from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Domestic(models.Model):
	title = models.CharField(max_length = 100)
	descriptions = RichTextUploadingField()
	date = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.title
		
	class Meta:
		verbose_name = 'Категорії'
		verbose_name_plural = 'Категорії'