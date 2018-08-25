from django.shortcuts import render, get_object_or_404
from video.models import Video
from django.template.context_processors import csrf

def video(request):
	video = Video.objects.all()
	return render(request, 'video/video.html', {'video':video})

def video_main(request, video_id):
	args = {}
	args.update(csrf(request))
	args['videos'] = Video.objects.get(id = video_id)
	return render(request, 'video/video_main.html', args)
