from django.contrib import admin

from .models import Thing
from .models import ThingCategory

admin.site.register(Thing)
admin.site.register(ThingCategory)
