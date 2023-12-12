# Generated by Django 4.2.8 on 2023-12-12 09:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_alter_posts_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='posts_liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
