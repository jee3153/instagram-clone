from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, reverse
from django.views.generic import ListView
from .models import FollowRelationship
from accounts.models import User


class FollowingsView(LoginRequiredMixin, ListView):

    login_url = "accounts:login"
    model = FollowRelationship
    template_name = "accounts/following_list.html"
    context_object_name = "followings"
    paginate_orphans = 5
    paginate_by = 25

    def get_queryset(self):
        followings_ids = FollowRelationship.objects.filter(
            follower=self.kwargs["user"]
        ).values_list("followings__id", flat=True)
        followings = (
            User.objects.prefetch_related("followings")
            .filter(pk__in=followings_ids)
            .order_by("username")
        )

        return followings


class FollowedView(LoginRequiredMixin, ListView):

    login_url = "accounts:login"
    model = FollowRelationship
    template_name = "accounts/followed_list.html"
    context_object_name = "followed"
    paginate_orphans = 5
    paginate_by = 25

    def get_queryset(self):
        followed_ids = FollowRelationship.objects.filter(
            follower=self.kwargs["user"]
        ).values_list("followed__id", flat=True)

        followed = (
            User.objects.prefetch_related("followed")
            .filter(pk__in=followed_ids)
            .order_by("username")
        )
        return followed


def follow_or_unfollow(request, author_pk, user_pk, follow):
    user = request.user
    author = User.objects.get(pk=author_pk)
    # relationship table for both author and user
    user_follow_table, _ = FollowRelationship.objects.get_or_create(follower=user)
    author_follow_table, _ = FollowRelationship.objects.get_or_create(follower=author)
    if user_pk != author_pk:
        # if this is following, add author to user's following list, user to author's followed list.
        if follow is True:
            user_follow_table.followings.add(author_pk)
            author_follow_table.followed.add(user_pk)
        # if this is following, remove author to user's following list, user to author's followed list.
        else:
            user_follow_table.followings.remove(author_pk)
            author_follow_table.followed.remove(user_pk)
    else:
        raise PermissionDenied
    return redirect(reverse("accounts:user", kwargs={"user": author_pk}))


@login_required(login_url="accounts:login")
def follow_user(request, author_pk, user_pk):
    return follow_or_unfollow(request, author_pk, user_pk, follow=True)


@login_required(login_url="accounts:login")
def unfollow_user(request, author_pk, user_pk):
    return follow_or_unfollow(request, author_pk, user_pk, follow=False)
