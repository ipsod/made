from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import inlineformset_factory
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView

from .models import Thing
from .models import ThingCategory
from .models import ThingAttribute
from .models import ThingAttributeValue
from .admin import ThingForm
from .admin import ThingAttributeValueForm


def index(request):
    categories = ThingCategory.objects.all()
    return render(request, 'catalog/category_list.html', {'categories': categories})


def category_detail(request, pk):
    category = get_object_or_404(ThingCategory, pk=pk)
    categories = category.children.all()

    # Get a paginated list of the Things in the category
    page = request.GET.get('page', 1)
    per_page = 3
    things = category.things.all()
    paginator = Paginator(things, per_page)
    try:
        things = paginator.page(page)
    except PageNotAnInteger:
        things = paginator.page(1)
    except EmptyPage:
        things = paginator.page(paginator.num_pages)

    context = {'category': category, 'categories': categories, 'things': things}
    return render(request, 'catalog/category.html', context)

class CategoryList(ListView):
    model = ThingCategory
    context_object_name = 'thing_category'

class CategoryUpdate(UpdateView):
    model = ThingCategory
    fields = '__all__'
    template_name_suffix = '_form'
    def get_success_url(self):
        return reverse('category_list', kwargs={
            'pk': self.object.pk,
        })

class CategoryCreate(CreateView):
    model = ThingCategory
    fields = '__all__'
    template_name_suffix = '_form'

    def get_success_url(self):
        return reverse('category_list', kwargs={
            'pk': self.object.pk,
        })

class CategoryDelete(DeleteView):
    model = ThingCategory

    def get_success_url(self):
        return reverse('category_list')


class AttributeDetail(DetailView):
    model = ThingAttribute
    context_object_name = 'thing_attribute'

    def get_context_data(self, **kwargs):
        context = super(AttributeDetail, self).get_context_data(**kwargs)
        context['thing_categories'] = self.object.thing_categories.all()
        return context

class AttributeList(ListView):
    model = ThingAttribute
    context_object_name = 'thing_attribute'

class AttributeUpdate(UpdateView):
    model = ThingAttribute
    fields = '__all__'
    template_name_suffix = '_form'

    def get_success_url(self):
        return reverse('attribute_list')

class AttributeCreate(CreateView):
    model = ThingAttribute
    fields = '__all__'
    template_name_suffix = '_form'

    def get_success_url(self):
        return reverse('attribute_list', kwargs={
            'pk': self.object.pk,
        })

class AttributeDelete(DeleteView):
    model = ThingAttribute

    def get_success_url(self):
        return reverse('attribute_list')


def thing_detail(request, thing_sku):
    thing = get_object_or_404(Thing, sku=thing_sku)
    values = thing.attribute_values.all()
    attributes = [(v.thing_attribute.name, v.value) for v in values]
    categories = thing.categories.all()

    context = {'thing': thing, 'categories': categories, 'attributes': attributes}
    return render(request, 'catalog/detail.html', context)

def create_thing(request, thing_sku, category_id):
    category = get_object_or_404(ThingCategory, id=category_id)
    thing = Thing(sku=thing_sku, entered=False)
    thing.save()
    thing.categories.add(category)
    return redirect('thing_edit', thing_sku=thing_sku)

def edit_thing(request, thing_sku):
    thing = get_object_or_404(Thing, sku=thing_sku)
    thing.rectify_attribute_values()
    ThingAttributeValueFormSet = inlineformset_factory(Thing, ThingAttributeValue, form=ThingAttributeValueForm, extra=0)
    if request.method == "POST":
        thing_form = ThingForm(request.POST, request.FILES, instance=thing)
        value_formset = ThingAttributeValueFormSet(request.POST, request.FILES, instance=thing)
        if thing_form.is_valid() and value_formset.is_valid():
            thing = thing_form.save(commit=False)
            value_formset.save()
            thing.save()
            thing_form.save_m2m()
            return redirect('thing_list', thing_sku=thing.sku)
    else:
        thing_form = ThingForm(instance=thing)
        value_formset = ThingAttributeValueFormSet(instance=thing)

    context = {'thing_form': thing_form, 'value_formset': value_formset}
    return render(request, 'catalog/thing_form.html', context)

class ThingDelete(DeleteView):
    model = Thing

    def get_success_url(self):
        return reverse('thing_list')
