from django.shortcuts import redirect, render
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
