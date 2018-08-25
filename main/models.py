from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

SHORT_ABOUT = 445

class About(models.Model):
	title = models.CharField(max_length = 100)
	descrip = RichTextUploadingField()
	img = models.ImageField(upload_to = 'about_photo', blank = True, null = True)


	def __str__(self):
		return self.title

	def get_short_desc(self):
		if len(self.descrip) > SHORT_ABOUT:
			return self.descrip[:SHORT_ABOUT]
		else:
			return self.descrip

	class Meta:
		verbose_name = 'Інформація про лікаря'
		verbose_name_plural = 'Інформація про лікаря'

class AboutMed(models.Model):
	title = models.CharField(max_length = 100)
	descrip = RichTextUploadingField()
	img = models.ImageField(upload_to = 'about_photo', blank = True, null = True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Інформація про медсестру'
		verbose_name_plural = 'Інформація про медсестру'

class SeasonNote(models.Model):
	title = models.CharField(max_length = 100)
	descriptions = RichTextUploadingField()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Сезонні нотатки'
		verbose_name_plural = 'Сезонні нотатки'