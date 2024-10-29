# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 09:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tournaments', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='name')),
                ('priority', models.IntegerField(help_text='Venues with a higher priority number will be preferred when allocating venues to debates', verbose_name='priority')),
                ('tournament', models.ForeignKey(blank=True, help_text='Venues not assigned to any tournament can be shared between tournaments', null=True, on_delete=django.db.models.deletion.CASCADE, to='tournaments.Tournament', verbose_name='tournament')),
            ],
            options={
                'verbose_name_plural': 'venues',
                'verbose_name': 'venue',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='VenueCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of category, e.g., "Purple", "Step-free access", "Close to tab room". This name is shown when the category is prefixed or suffixed to a venue name in the draw, e.g., "Purple – G05".', max_length=80, verbose_name='name')),
                ('description', models.CharField(blank=True, help_text='Description, as the predicate of a sentence, e.g. "has step-free access", "is close to the briefing hall". This description follows "This venue" when shown in tooltips, e.g., "This venue is close to the briefing hall.".', max_length=200, verbose_name='description')),
                ('display_in_venue_name', models.CharField(choices=[('-', "Don't display in venue name"), ('P', 'Display as prefix'), ('S', 'Display as suffix')], default='-', help_text='Prefix: "Purple – G05", Suffix: "G05 – Purple"', max_length=1, verbose_name='display in venue name')),
                ('display_in_public_tooltip', models.BooleanField(default=False, help_text='Displays the description in the tooltip for the venue on public pages. The description, if not blank, will always show on admin pages.', verbose_name='display in public tooltip')),
                ('venues', models.ManyToManyField(blank=True, to='venues.Venue', verbose_name='venues')),
            ],
            options={
                'verbose_name': 'venue category',
                'verbose_name_plural': 'venue categories',
            },
        ),
        migrations.CreateModel(
            name='VenueConstraint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField(verbose_name='priority')),
                ('subject_id', models.PositiveIntegerField(verbose_name='subject ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venues.VenueCategory', verbose_name='category')),
                ('subject_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='subject content type')),
            ],
            options={
                'verbose_name': 'venue constraint',
                'verbose_name_plural': 'venue constraints',
            },
        ),
        migrations.AlterIndexTogether(
            name='venue',
            indexes=[models.Index(fields=[('name',)])],
        ),
    ]
