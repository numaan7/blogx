# Generated by Django 3.2.12 on 2022-02-27 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_auto_20220227_1416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='parent',
        ),
        migrations.AddField(
            model_name='comments',
            name='reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='web.comments'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='featured_image/%Y/%m/%d/'),
        ),
    ]
