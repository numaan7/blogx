# Generated by Django 3.2.12 on 2022-02-27 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_auto_20220227_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.comments'),
        ),
        migrations.AddField(
            model_name='comments',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
