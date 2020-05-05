from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreateUserForm
from .decorators import unauthenticated_user


@unauthenticated_user
def register_view(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, f"Account was created for {user}.")
            return redirect(reverse("accounts:login"))
    context = {"form": form}
    return render(request, "accounts/register.html", context)


@unauthenticated_user
def login_view(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password1")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print(user)
            return redirect(reverse("core:home"))
        else:
            messages.info(request, "Username OR password is incorrect")
    form = UserCreationForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)


def logout_user(request):
    logout(request)
    return redirect(reverse("accounts:login"))


@login_required(login_url="accounts:login")
def setting_view(request, user):
    if request.user == user:
        print("correct User")
    return render(request, "accounts/setting.html")
