# Generated by Django 2.2.6 on 2020-10-28 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloglist',
            name='desc',
            field=models.TextField(default='sample'),
        ),
    ]
