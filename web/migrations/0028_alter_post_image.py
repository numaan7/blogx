# Generated by Django 3.2.12 on 2022-02-28 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0027_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='blog/media/featured_image/2022/02/18/fi.jpg', upload_to='featured_image/%Y/%m/%d/'),
        ),
    ]
