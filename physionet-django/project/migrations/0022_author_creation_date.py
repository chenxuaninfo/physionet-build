# Generated by Django 2.1.7 on 2019-05-21 00:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0021_auto_20190502_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]