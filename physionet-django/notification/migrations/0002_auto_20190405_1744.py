# Generated by Django 2.1.7 on 2019-04-05 21:44

from django.db import migrations
import project.models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content',
            field=project.models.SafeHTMLField(),
        ),
    ]
