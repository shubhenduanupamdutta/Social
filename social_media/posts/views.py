from django.shortcuts import get_object_or_404, redirect, render
from .models import Posts
from .forms import CommentForm, PostCreateForm
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
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        new_comment = comment_form.save(commit=False)
        post_id = request.POST.get("post_id")
        post = get_object_or_404(Posts, id=post_id)
        new_comment.post = post
        new_comment.posted_by = request.user
        new_comment.save()

        return redirect("feed")

    comment_form = CommentForm()
    posts = Posts.objects.all()
    context = {"form": comment_form, "posts": posts}
    return render(request, "posts/feed.html", context)


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
