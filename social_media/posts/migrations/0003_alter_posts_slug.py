# Generated by Django 4.2.8 on 2023-12-08 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_posts_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='slug',
            field=models.SlugField(blank=True, max_length=200),
        ),
    ]
