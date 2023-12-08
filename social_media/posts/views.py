from django.shortcuts import redirect, render
from .forms import PostCreateForm


# Create your views here.
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
