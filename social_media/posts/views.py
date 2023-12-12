from django.shortcuts import get_object_or_404, redirect, render
from .models import Posts
from .forms import PostCreateForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def post_create(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()

        return redirect("index")

    form = PostCreateForm()
    return render(request, "posts/post_create.html", {"form": form})


def feed(request):
    posts = Posts.objects.all()
    return render(request, "posts/feed.html", {"posts": posts})


def like_post(request):
    post_id = request.POST.get("post_id")
    post = get_object_or_404(Posts, id=post_id)
    user = request.user
    response = {}
    if user in post.liked_by.all():
        post.liked_by.remove(user)
        response["message"] = "unlike"
    else:
        post.liked_by.add(user)
        response["message"] = "like"

    return redirect("feed")
