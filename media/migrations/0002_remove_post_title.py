# Generated by Django 3.2.5 on 2021-07-18 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]
