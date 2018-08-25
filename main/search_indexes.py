import datetime
from haystack import indexes
from main.models import About


class AboutIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	title = indexes.CharField(model_attr = 'title')
	# date = indexes.DateTimeField(model_attr='date')

	def get_model(self):
		return About

	def index_queryset(self, using=None):
		return self.get_model().objects.all()
		# return self.get_model().objects.filter(date__lte=datetime.datetime.now())

