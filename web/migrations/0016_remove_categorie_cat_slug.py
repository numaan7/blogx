# Generated by Django 3.2.12 on 2022-02-27 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_categorie_cat_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorie',
            name='cat_slug',
        ),
    ]
