# Generated by Django 2.1.7 on 2019-04-02 19:15

from django.db import migrations, models
import project.validators


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_auto_20190325_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publishedproject',
            name='is_newest_version',
        ),
        migrations.RemoveField(
            model_name='publishedproject',
            name='newest_version',
        ),
        migrations.AddField(
            model_name='activeproject',
            name='is_new_version',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='archivedproject',
            name='is_new_version',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='publishedproject',
            name='has_other_versions',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='publishedproject',
            name='is_latest_version',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='activeproject',
            name='slug',
            field=models.SlugField(max_length=20),
        ),
        migrations.AlterField(
            model_name='activeproject',
            name='version',
            field=models.CharField(blank=True, default='', max_length=15, validators=[project.validators.validate_version]),
        ),
        migrations.AlterField(
            model_name='archivedproject',
            name='slug',
            field=models.SlugField(max_length=20),
        ),
        migrations.AlterField(
            model_name='archivedproject',
            name='version',
            field=models.CharField(blank=True, default='', max_length=15, validators=[project.validators.validate_version]),
        ),
        migrations.AlterField(
            model_name='publishedproject',
            name='slug',
            field=models.SlugField(max_length=20),
        ),
        migrations.AlterField(
            model_name='publishedproject',
            name='version',
            field=models.CharField(blank=True, default='', max_length=15, validators=[project.validators.validate_version]),
        ),
        migrations.AlterField(
            model_name='storagerequest',
            name='response_message',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]
