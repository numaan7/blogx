# Generated by Django 3.2.12 on 2022-02-27 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_remove_categorie_cat_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorie',
            old_name='cat_name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.categorie'),
        ),
    ]
