from django.contrib import admin

from .models import Comment, Posts


# Register your models here.
admin.site.register(Posts)
admin.site.register(Comment)
