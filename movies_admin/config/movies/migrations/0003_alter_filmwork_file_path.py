# Generated by Django 3.2 on 2023-07-02 08:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('movies', '0002_auto_20230702_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmwork',
            name='file_path',
            field=models.TextField(blank=True, null=True,
                                   verbose_name='file_path'),
        ),
    ]
