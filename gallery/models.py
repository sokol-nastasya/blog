from django.db import models

class Photo(models.Model):
	title = models.CharField(max_length = 300, blank = True)
	img = models.ImageField(upload_to = 'gallery_img', blank = True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Фото'
		verbose_name_plural = 'Фото'