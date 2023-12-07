from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from .forms import LoginForm

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
