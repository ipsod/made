from django.db import models

from model_utils import Choices
from mptt.models import MPTTModel, TreeForeignKey


class ThingCategory(MPTTModel):
    class Meta:
        verbose_name_plural = "thing categories"

    name = models.CharField(max_length=200)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', db_index=True)
    description = models.TextField(max_length=200, blank=True)

    # TODO This still allows root nodes to have the same name
    class Meta:
        unique_together = (('name', 'parent', ), )
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Thing(models.Model):
    CONDITION = Choices('new', 'new-other', 'used')
    DEFAULT_ATTRIBUTES = {'artist': 'Dusty Gamble'}

    sku = models.IntegerField(unique=True)
    entered = models.BooleanField()
    name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    condition = models.CharField(choices=CONDITION, default=CONDITION.new, max_length=20)
    condition_description = models.TextField(blank=True)
    categories = models.ManyToManyField(ThingCategory, related_name='things')
    featured_in_categories = models.ManyToManyField(ThingCategory, related_name='featured_things', blank=True)
    # attribute_values
    # TODO location = models.ForeignKey(Location)


    def __str__(self):
        return "Thing " + str(self.sku)


    def rectify_attribute_values(self, delete_extras=True):
        '''
        Add any ThingAttributeValues the thing is missing.
        Remove any ThingAttributeValues the thing doesn't need.
        '''

        thing_attribute_values = self._get_thing_attribute_values()
        category_attributes = self._get_category_attributes()

        # Create any values the thing is missing
        for name, attribute in category_attributes.items():
            if name in thing_attribute_values:
                thing_attribute_values.pop(name)  # Any values left after looping do not belong
            else:
                default = ''
                if name in self.DEFAULT_ATTRIBUTES:
                    default = self.DEFAULT_ATTRIBUTES[name]
                attribute_value = ThingAttributeValue(thing_attribute=attribute, thing=self, value=default)
                attribute_value.save()

        # Delete any values the thing has, but don't belong in the category
        if delete_extras and thing_attribute_values and False:
            for thing_attribute_value in thing_attribute_values:
                thing_attribute_value.delete()


    def _get_thing_attribute_values(self):
        '''
        Gather ThingAttributeValues into a dict with ThingAttribute.name as key
        '''
        # Gather thing attributes into a dict
        values = {}
        thing_attribute_values = self.attribute_values.all()
        for thing_attribute_value in thing_attribute_values:
            attribute = thing_attribute_value.thing_attribute
            values[attribute.name] = thing_attribute_value
        return values


    def _get_category_attributes(self):
        '''
        Gather Category.ThingAttributes into a dict with ThingAttribute.name as key
        '''
        category_attributes = {}
        category_thing_attribute_sets = [c.thing_attributes.all() for c in self.categories.order_by('-name').all()]
        for category_attribute_set in category_thing_attribute_sets:
            for category_attribute in category_attribute_set:
                category_attributes[category_attribute.name] = category_attribute

        return category_attributes


    def get_initial_attributes(self):
        thing_attribute_values = self._get_thing_attribute_values()
        category_attributes = self._get_category_attributes()


        initial = []
        for name, attribute in all_attributes.items():
            row = {'thing_attribute': attribute}
            if name in values:
                row['value'] = values[name].value
                row['id'] = values[name].id
            initial.append((row))

        return initial


class ThingAttribute(models.Model):
    '''
    reference:
    django-eav
    https://docs.djangoproject.com/en/1.9/topics/forms/formsets/
    http://stackoverflow.com/questions/3712688/creation-of-dynamic-model-fields-in-django
    '''

    thing_categories = models.ManyToManyField(ThingCategory, related_name='thing_attributes')
    name  = models.CharField(max_length=200, unique=True)
    # tooltip = models.CharField(max_length=200, blank=True, null=True, )
    # description = models.TextField(blank=True, null=True, )
    # suggest_previous = models.BooleanField()  # lets user select from previously used options or add a new one

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class ThingAttributeValue(models.Model):
    thing = models.ForeignKey(Thing, related_name='attribute_values')
    thing_attribute = models.ForeignKey(ThingAttribute, related_name='attribute_values')
    value = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        unique_together = (('thing', 'thing_attribute', ), )
        ordering = ['thing_attribute__name']
