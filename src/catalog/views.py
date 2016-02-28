from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Thing
from .models import ThingCategory


def index(request):
    categories = ThingCategory.objects.all()

    context = {'categories': categories}
    return render(request, 'catalog/category_list.html', context)
    pass


def category_detail(request, category_id):
    category = get_object_or_404(ThingCategory, id=category_id)
    categories = category.children.all()

    page = request.GET.get('page', 1)
    per_page = 3

    things = category.thing_set.all()
    paginator = Paginator(things, per_page)

    try:
        things = paginator.page(page)
    except PageNotAnInteger:
        things = paginator.page(1)
    except EmptyPage:
        things = paginator.page(paginator.num_pages)

    context = {'category': category, 'categories': categories, 'things': things}
    return render(request, 'catalog/category.html', context)
    pass


def detail(request, thing_sku):
    thing = get_object_or_404(Thing, sku=thing_sku)
    categories = thing.categories.all()

    context = {'thing': thing, 'categories': categories}

    return render(request, 'catalog/detail.html', context)
