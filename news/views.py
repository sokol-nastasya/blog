from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.template.context_processors import csrf

from news.models import News, Keywords

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import date


def news_page(request):
	news_list = News.objects.all().order_by('-date')
	keywords = Keywords.objects.all()

	query = request.GET.get("q")
	if query:
		news_list = news_list.filter(title__icontains = query)
	paginator = Paginator(news_list, 6)
	page = request.GET.get('page')

	try:
		news = paginator.page(page)
	except PageNotAnInteger:
		news = paginator.page(1)
	except EmptyPage:
		news = paginator.page(paginator.num_pages)

	context = {'news': news, 'keywords': keywords}
	return render(request, 'news/news_page.html', context)

def show_news_page(request, show_news_id):
	args = {}
	args.update(csrf(request))
	args['news_list'] = get_object_or_404(News, id = show_news_id)
	return render(request, 'news/news.html', args)


def keywords(request, k_id):
    keywords = Keywords.objects.all()
    args = {}
    args['keywords'] = Keywords.objects.all()
    args['keys'] = Keywords.objects.get(id = k_id)
    args['news'] = News.objects.filter(keywords__name__exact = args['keys'])
    return render(request, 'news/keypage.html', args)
