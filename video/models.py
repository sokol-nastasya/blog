from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from embed_video.fields import EmbedVideoField

SHORT_TEXT_LEN = 70

class Video(models.Model):
	title = models.CharField(max_length = 200)
	descriptions = RichTextUploadingField()
	date = models.DateTimeField()
	video = EmbedVideoField(blank = True, null = True)
   
	def __str__(self):
		return self.title

	def get_short_descr(self):
		if len(self.descriptions) > SHORT_TEXT_LEN:
			return self.descriptions[:SHORT_TEXT_LEN]
		else:
			return self.descriptions

	class Meta:
		verbose_name = 'Відео'
		verbose_name_plural = 'Відео'