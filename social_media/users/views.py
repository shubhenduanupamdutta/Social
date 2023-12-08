from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from posts.models import Posts
from .forms import LoginForm, UserRegisterForm, UserEditForm, ProfileEditForm
from .models import Profile

# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # process form data
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponse(
                    f"Welcome {user.username}! you are logged in.")  # type: ignore # noqa
            else:
                return HttpResponse("Invalid login details supplied.")

    form = LoginForm()
    return render(request, 'users/login.html', context={'form': form})


@login_required
def index(request):
    current_user = request.user
    user_posts = Posts.objects.filter(user=current_user)
    return render(request, 'users/index.html', {"posts": user_posts})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # process form data
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Profile.objects.create(user=user)
            return render(request, 'users/register_done.html')

    form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

        return redirect('index')

    user_form = UserEditForm(instance=request.user)
    profile_form = ProfileEditForm(instance=request.user.profile)

    context = {"user_form": user_form, "profile_form": profile_form}
    return render(request, 'users/edit.html', context=context)
