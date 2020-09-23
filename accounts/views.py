from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.http import Http404, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import View
from .forms import CreateUserForm, EditProfileForm, SearchForm
from .decorators import unauthenticated_user
from photos.models import Photo
from .models import User
from follow.models import FollowRelationship


@login_required(login_url="accounts:login")
def user_view(request, user):
    try:
        # author = User.objects.get(pk=user)
        author = get_object_or_404(User, pk=user)
        posts = Photo.objects.filter(author_id=user)
        author_followed_ids = FollowRelationship.objects.filter(
            follower=user
        ).values_list("followed__id", flat=True)
        author_followings_ids = FollowRelationship.objects.filter(
            follower=user
        ).values_list("followings__id", flat=True)

        def follow_counter(qs):
            if None in qs:
                return "0"
            else:
                return qs.count()

    except User.DoesNotExist:
        raise Http404("User does not exist")

    context = {
        "posts": posts,
        "author": author,
        "followed": author_followed_ids,
        "followed_count": follow_counter(author_followed_ids),
        "followings_count": follow_counter(author_followings_ids),
    }
    return render(request, "accounts/user_view.html", context)


def logout_user(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect(reverse("accounts:login"))


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
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print(user)
            return redirect(reverse("core:home"))
        else:
            messages.info(request, "Username OR password is incorrect")

    context = {"form": form}
    return render(request, "accounts/login.html", context)


@login_required(login_url="accounts:login")
def setting_view(request, user):
    if request.user.pk != user:
        raise PermissionDenied
    else:
        me = request.user
        form = EditProfileForm(instance=me)
        if request.method == "POST":
            form = EditProfileForm(request.POST, request.FILES, instance=me)
            if form.is_valid():
                form.save()
                print(request.POST)
                print(request.FILES)
                return JsonResponse(
                    {
                        "error": False,
                        "message": "Uploaded Successfully",
                        "media": request.user.profile.name,
                    }
                )
            else:
                return JsonResponse({"error": True, "errors": form.errors})
        else:
            context = {"form": form}
            return render(request, "accounts/setting.html", context)


class SearchView(LoginRequiredMixin, View):
    model = User
    login_url = "accounts:login"

    def get(self, request):
        form = SearchForm()
        if request.method == "GET":
            form = SearchForm(request.GET)
            if form.is_valid():
                keyword = form.cleaned_data.get("username")

                filter_args = {}
                filter_args["username__istartswith"] = keyword
                queryset = User.objects.filter(**filter_args).order_by("username")

                paginator = Paginator(object_list=queryset, per_page=25, orphans=5)
                page = request.GET.get("page")
                users = paginator.get_page(page)
                print(users)
                print(vars(users.paginator))
                context = {"form": form, "users": users, "keyword": keyword}
                return render(request, "accounts/search.html", context)
        context = {"form": form}
        return render(request, "accounts/search.html", context)
