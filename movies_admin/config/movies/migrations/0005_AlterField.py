# Generated by Django 3.2 on 2023-07-03 09:27

import django.core.validators

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_person_filmwork'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmwork',
            name='creation_date',
            field=models.DateField(null=True, verbose_name='Creation_date'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='file_path',
            field=models.TextField(blank=True, default='', verbose_name='file_path'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='rating',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Rating'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='type',
            field=models.CharField(blank=True, choices=[('MOV', 'movie'), ('TVS', 'tv_show')], default='', max_length=30, verbose_name='type'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='genre',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='personfilmwork',
            name='role',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Role'),
            preserve_default=False,
        ),
    ]