from django.shortcuts import render, render_to_response, get_object_or_404
from articles.models import Category, Article
from django.template.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def article_cat(request):
	main_list = Article.objects.all()
	
	query = request.GET.get("q")
	if query:
		main_list = main_list.filter(main_service__icontains = query)
	paginator = Paginator(main_list, 4)

	page = request.GET.get('page')
	try:
		articles_list = paginator.page(page)
	except PageNotAnInteger:
		articles_list = paginator.page(1)
	except EmptyPage:
		articles_list = paginator.page(paginator.num_pages)

	context = {
				'articles_list': articles_list, 
				'categories': Category.objects.all(), 
				
				}
	return render(request, 'articles/article_cat.html', context)

def article(request, article_id):
	args = {}
	args.update(csrf(request))
	args['article_list'] = get_object_or_404(Article, id = article_id)
	return render(request, 'articles/article.html', args)

def category(request, category_id):
	args = {}
	args['categories'] = Category.objects.all() 
	args['category'] = Category.objects.get(id = category_id)
	args['articles_list'] = Article.objects.filter(category_id = category_id)
	return render_to_response('articles/category.html', args)