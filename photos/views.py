from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sessions.backends.db import SessionStore
from django.core.exceptions import PermissionDenied
from django.http import Http404, JsonResponse, HttpResponse, HttpRequest
from django.contrib import messages
from .models import Photo, Likes
from accounts.models import User
from follow.models import FollowRelationship
from django.views.generic import UpdateView, ListView, View, DetailView
from .forms import PostForm, SearchForm
import random
import string


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    result = "".join(random.choice(chars) for i in range(size))
    return result


def guest_user(username):
    return "Guest user" in username


# @login_required(login_url="accounts:login")
def home_view(request):
    posts = Photo.objects.all()
    # user_id = request.COOKIES["user_id"]

    # if guest_user(request.user) and user_id is None:
    #     try:
    #         generated_name = id_generator()
    #         user = User(username=f"Guest user{generated_name}")
    #         user.set_unusable_password()
    #         user.save()
    #         request.user = user
    #         HttpResponse.set_cookie(key="username", value=user.username)
    #         HttpResponse.set_cookie(key="password", value=user.password)

    #     except Exception:
    #         pass
    # elif user_id is not None:
    #     request.user = User.objects.get(pk=user_id)

    # elif request.user.is_authenticated:
    #     pass

    is_guest_user = guest_user(request.user.username)

    context = {"posts": posts, "is_guest_user": is_guest_user}
    response = render(request, "photos/time_feed.html", context)

    return response


# @login_required(login_url="accounts:login")
def user_view(request, user):
    try:
        photos = Photo.objects.filter(pk=user)

    except Photo.DoesNotExist:
        raise Http404("User does not exist")
    return render(
        request, "photos/user_photos.html", {"photos": photos, "author": user}
    )


@login_required(login_url="accounts:login")
def newpost_view(request, user):
    if request.user.pk != user:
        raise PermissionDenied
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Your photo posted.")
            return redirect(reverse("core:home"))
    else:
        messages.error(request, "Something went wrong.")
        form = PostForm()
    return render(request, "photos/new_photo.html", {"form": form})


@login_required(login_url="accounts:login")
def deletepost_view(request, author_pk, photo_pk):
    post = get_object_or_404(Photo, pk=photo_pk)
    if request.user.pk is author_pk:
        post.delete()
        messages.success(request, "Post deleted.")
    return redirect(reverse("core:home"))


class EditPost(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Photo
    pk_url_kwarg = "photo_pk"
    template_name = "photos/edit_photo.html"
    form_class = PostForm
    success_message = "Post Edited."
    login_url = "accounts:login"


@login_required(login_url="accounts:login")
def like_photo(request, photo_pk, user_pk):
    photo = Photo.objects.get(pk=photo_pk)
    post_table, created = Likes.objects.get_or_create(photo=photo)
    likers = photo.post.likers
    # if request.user.pk is None:
    #     return redirect(reverse("accounts:login"))
    if request.user not in likers.all():
        likers.add(user_pk)
        return redirect(reverse("core:home"))


@login_required(login_url="accounts:login")
def unlike_photo(request, photo_pk, user_pk):
    photo = Photo.objects.get(pk=photo_pk)
    likers = photo.post.likers
    if request.user in likers.all():
        likers.remove(user_pk)
    return redirect(reverse("core:home"))


class LikeList(ListView):
    model = Likes
    context_object_name = "likers"
    template_name = "photos/likes_list.html"

    def get_queryset(self):
        likers_id = Likes.objects.filter(photo_id=self.kwargs["photo_pk"]).values_list(
            "likers__id", flat=True
        )
        likers = User.objects.prefetch_related("likers").filter(pk__in=likers_id)
        return likers

    def get_context_data(self, *, object_list=None, **kwargs):
        photo = Photo.objects.get(pk=self.kwargs["photo_pk"])
        context = super(LikeList, self).get_context_data(**kwargs)
        context["author"] = photo.author
        return context


class SearchView(LoginRequiredMixin, View):
    model = Photo
    login_url = "accounts:login"

    def get(self, request):
        form = SearchForm()
        if request.method == "GET":
            form = SearchForm(request.GET)
            if form.is_valid():
                keyword = form.cleaned_data.get("content")

                filter_args = {}
                filter_args["content__icontains"] = keyword
                queryset = Photo.objects.filter(**filter_args).order_by("content")

                page = request.GET.get("page")
                paginator = Paginator(object_list=queryset, per_page=15, orphans=5)
                posts = paginator.get_page(page)

                context = {
                    "form": form,
                    "posts": posts,
                    "keyword": keyword,
                }
                return render(request, "photos/search.html", context)
        context = {"form": form}
        return render(request, "photos/search.html", context)


class PostDetail(DetailView):
    model = Photo


# original home_view

# def home_view(request):

#     try:
#         filtering photos by user's followings
#         user_id = User.objects.filter(pk=user.id).values_list("id", flat=True)
#         followings_ids = FollowRelationship.objects.filter(follower=user).values_list(
#             "followings__id", flat=True
#         )

#         lookup_user_ids = followings_ids.union(user_id)
#         posts_by_followers_and_user = Photo.objects.prefetch_related(
#             "author__followings"
#         ).filter(author__in=lookup_user_ids)

#     except FollowRelationship.DoesNotExist:
#         pass

#     context = {
#         "posts": posts,
#         "followings": followings_ids,
#     }

#     return render(request, "photos/time_feed.html", context)
