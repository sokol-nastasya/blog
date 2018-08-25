from django.shortcuts import render
from category.models import Domestic

# Create your views here.
def cat(request):
	return render(request, 'category/cat.html')

def domestic(request):
	args = Domestic.objects.all()
	context = {'args':args}
	return render(request, 'category/domestic.html', context)

def bacteria(request):
	return render(request, 'category/bacteria.html')

def cold(request):
	return render(request, 'category/cold.html')

def food(request):
	return render(request, 'category/food.html')

def pills(request):
	return render(request, 'category/pills.html')

def plants(request):
	return render(request, 'category/plants.html')

def asit(request):
	return render(request, 'category/asit.html')

def asthma(request):
	return render(request, 'category/asthma.html')

def child(request):
	return render(request, 'category/child.html')

def t_al(request):
	return render(request, 'category/t_al.html')