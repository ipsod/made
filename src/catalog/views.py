from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Thing
from .models import ThingCategory


def index(request):
    page = request.GET.get('page', 1)
    per_page = 3
    things = Thing.objects.all()
    paginator = Paginator(things, per_page)

    try:
        things = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        things = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        things = paginator.page(paginator.num_pages)

    context = {'things': things}
    return render(request, 'catalog/index.html', context)


def category(request, *category_id):

    if category_id:
        category = get_object_or_404(ThingCategory, pk=category_id)
        subcategories = ThingCategory.get_children()
    else:
        category = None
        subcategories = ThingCategory.objects.all()

    context = {'category': category, 'subcategories': subcategories}
    return render(request, 'catalog/catalog.html', context)


def detail(request, thing_id):
    thing = get_object_or_404(Thing, pk=thing_id)
    categories = thing.categories.all()

    return render(request, 'catalog/detail.html', {'thing': thing, 'categories': categories})
