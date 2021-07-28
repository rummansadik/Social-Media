# Generated by Django 3.2.5 on 2021-07-28 06:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_vote_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='amountofvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='votesubmitted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]