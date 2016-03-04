# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 01:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20160227_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThingAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ThingAttributeValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='thingcategory',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='thing',
            name='condition',
            field=models.CharField(choices=[('new', 'new'), ('new-other', 'new-other'), ('used', 'used')], default='new', max_length=20),
        ),
        migrations.AlterUniqueTogether(
            name='thingcategory',
            unique_together=set([('name', 'parent')]),
        ),
        migrations.AddField(
            model_name='thingattributevalue',
            name='thing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Thing'),
        ),
        migrations.AddField(
            model_name='thingattributevalue',
            name='thing_attribute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.ThingAttribute'),
        ),
        migrations.AddField(
            model_name='thingattribute',
            name='thing_categories',
            field=models.ManyToManyField(to='catalog.ThingCategory'),
        ),
        migrations.AlterUniqueTogether(
            name='thingattributevalue',
            unique_together=set([('thing', 'thing_attribute')]),
        ),
    ]
