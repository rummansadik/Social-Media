# Generated by Django 3.2.5 on 2021-07-21 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0010_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_pics'),
        ),
    ]