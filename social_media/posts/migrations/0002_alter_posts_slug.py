# Generated by Django 4.2.8 on 2023-12-08 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
    ]