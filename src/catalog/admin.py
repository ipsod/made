from django import forms
from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from .models import Thing
from .models import ThingCategory
from .models import ThingAttribute
from .models import ThingAttributeValue

# TODO: http://alexkehayias.tumblr.com/post/16186725117/how-to-overwrite-the-save-of-a-django-form-like-a


class ThingCategoryAdmin(DjangoMpttAdmin):
    pass


class ThingCategoryForm(forms.ModelForm):
    class Meta:
        model = ThingCategory
        exclude = ['featured_things']


class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        exclude = ['sku']


class ThingAttributeForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = '__all__'

class ThingAttributeValueForm(forms.ModelForm):
    class Meta:
        model = ThingAttributeValue
        fields = ['value']



class ThingAttributeValueInline(admin.TabularInline):
    model = ThingAttributeValue

class ThingAdmin(admin.ModelAdmin):
    form = ThingForm
    inlines = [
        ThingAttributeValueInline,
    ]


admin.site.register(Thing, ThingAdmin)
# admin.site.register(ThingCategory, ThingCategoryAdmin)
admin.site.register(ThingCategory)
admin.site.register(ThingAttribute)
admin.site.register(ThingAttributeValue)
