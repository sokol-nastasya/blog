from django.shortcuts import render

from gallery.models import Photo

def gallery(request):
	photos = Photo.objects.all()
	context = {'photos':photos}
	return render(request, 'gallery/maingallery.html', context)
