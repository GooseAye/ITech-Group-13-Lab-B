# Generated by Django 2.2.4 on 2022-03-14 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent_live', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lettingagent',
            name='like_help_jsons',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lettingagent',
            name='like_quality_jsons',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]