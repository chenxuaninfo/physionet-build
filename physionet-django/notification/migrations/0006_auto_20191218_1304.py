# Generated by Django 2.2.6 on 2019-12-18 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0005_auto_20190502_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='front_page_banner',
            field=models.BooleanField(default=False),
        ),
    ]
