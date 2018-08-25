from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from haystack.forms import SearchForm
from haystack.generic_views import SearchView
from datetime import date


from main.models import About, SeasonNote, AboutMed


class MySearchView(SearchView):

    template_name = 'search/search.html'

    def get_queryset(self):
        queryset = super(MySearchView, self).get_queryset()
        return queryset.filter(date__gte=date(2018,1,1))

    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        return context


def main(request):
	note = SeasonNote.objects.all()
	context = {'note': note}
	return render(request, 'main/home.html', context)

def about(request):
    infs = About.objects.all()
    med = AboutMed.objects.all()
    context = {'infs':infs, 'med':med}
    return render(request, 'main/about.html', context)

def contact(request):
    return render(request, 'main/contact.html')

def calendar(request):
    return render(request, 'main/calendar.html')


def media(request):
    return render(request, 'main/media.html')

def certificates(request):
    return render(request, 'main/certificates.html')

def photo(request):
    return render(request, 'main/photo.html')