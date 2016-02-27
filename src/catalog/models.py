from django.db import models

from model_utils import Choices
from mptt.models import MPTTModel, TreeForeignKey


class ThingCategory(MPTTModel):
    class Meta:
        verbose_name_plural = "thing categories"

    name = models.CharField(max_length=200)
    parent = TreeForeignKey('self', null=True, related_name='children', db_index=True)
    description = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.name
    # inherit_attributes = models.BooleanField(default=True)


# #  http://stackoverflow.com/questions/3712688/creation-of-dynamic-model-fields-in-django
# class ThingAttribute(models.Model):
#     thing_category = models.ManyToManyField(ThingCategory)
#     name  = models.CharField()  # TODO All functions and attributes of Thing should be restricted names
#     is_enum = models.BooleanField()  # lets user select from previously used options or add a new one
#
#
# class ThingAttributeValue(models.Model):
#     thing_attribute = models.ForeignKey(ThingAttribute)
#     value = models.CharField()



class Thing(models.Model):
    sku = models.IntegerField(unique=True)
    name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    CONDITION = Choices('new', 'new-other', 'used', 'vintage', 'antique')
    condition = models.CharField(choices=CONDITION, default=CONDITION.new, max_length=20)
    condition_description = models.TextField(blank=True)

    def __str__(self):
        return "Thing " + str(self.sku)
    categories = models.ManyToManyField(ThingCategory)
#     attributes = models.ManyToManyField(ThingAttributeValue)
#     location = models.ForeignKey(Location)


    # Measurements
    # length_in_cm = models.TextField(max_length=200, blank=True)
    # diameter_in_cm = models.TextField(max_length=200, blank=True)
    # hole_size_in_cm = models.TextField(max_length=200, blank=True)
    # spin_time_in_seconds = models.TextField(max_length=200, blank=True)

    # Art-specific stuff
    # signature = models.CharField(max_length=200, blank=True)

    # have measurements
    #     for example
    #         diameter
    #         height
    #         hole size (for beads and pendants)
    #         spin time (spinning tops only)
    #     could be extensible to add other measurements, or is it much easier to explicitly define what measurements may be used?
    #     it would be nice if measurements could be converted to metric for international users
    # have a category
    #     spinning tops, marbles, pendants, etc.
    # have an active listing
    #    ebay #3743743273
    #    shopify https://shop.dusty.glass/green-glow-marble
    # have a style
