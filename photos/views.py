from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.http import Http404
from . import models as photo_models
from accounts import models as user_models
from . import forms


@login_required(login_url="accounts:login")
def home_view(request):
    posts = photo_models.Photo.objects.all()
    return render(request, "photos/time_feed.html", {"posts": posts})


@login_required(login_url="accounts:login")
def user_view(request, user):
    try:
        photos = photo_models.Photo.objects.filter(pk=user)
    except photo_models.Photo.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, "photos/user_photos.html", {"photos": photos})


@login_required(login_url="accounts:login")
def create_view(request, user):
    if request.method == "POST":
        form = forms.PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(reverse("core:home"))
    else:
        form = forms.PostForm()
    return render(request, "photos/new_photo.html", {"form": form})


@login_required(login_url="accounts:login")
def edit_view(request, user):
    return render(request, "photos/edit_photo")
