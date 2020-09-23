from django.urls import path
from . import views

app_name = "follow"


urlpatterns = [
    path("<int:user>/followings/", views.FollowingsView.as_view(), name="followings"),
    path("<int:user>/followed/", views.FollowedView.as_view(), name="followed"),
    path(
        "<int:author_pk>/followuser/<int:user_pk>/",
        views.follow_user,
        name="followuser",
    ),
    path(
        "<int:author_pk>/unfollowuser/<int:user_pk>/",
        views.unfollow_user,
        name="unfollowuser",
    ),
]
