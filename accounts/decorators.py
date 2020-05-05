from django.http import HttpResponse
from django.shortcuts import redirect, reverse


def unauthenticated_user(view_func):
    def wrapper_func(request, *arg, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse("core:home"))
        else:
            return view_func(request, *arg, **kwargs)

    return wrapper_func
