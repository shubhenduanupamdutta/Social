from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .forms import LoginForm, UserRegisterForm
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
    return render(request, 'users/index.html')


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
