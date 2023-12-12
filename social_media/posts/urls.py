from django.urls import path
from . import views

urlpatterns = [
    path("feed/", views.feed, name="feed"),
    path("create/", views.post_create, name="create"),
    path("like/", views.like_post, name="like"),
]
