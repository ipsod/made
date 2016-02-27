from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Thing


def index(request):
    page = request.GET.get('page', 1)
    per_page = 3
    things = Thing.objects.all()
    paginator = Paginator(things, per_page)

    try:
        things = paginator.page(page)
    except PageNotAnInteger:
        things = paginator.page(1)
    except EmptyPage:
        things = paginator.page(paginator.num_pages)

    context = {'things': things}
    return render(request, 'catalog/index.html', context)


def detail(request, thing_id):
    thing = get_object_or_404(Thing, pk=thing_id)

    return render(request, 'catalog/detail.html', {'thing': thing})
