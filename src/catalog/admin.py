from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from .models import Thing
from .models import ThingCategory


class ThingCategoryAdmin(DjangoMpttAdmin):
    pass


admin.site.register(Thing)
# admin.site.register(ThingCategory, ThingCategoryAdmin)
admin.site.register(ThingCategory)
