from django.urls import path
from . import views

app_name = "photos"


urlpatterns = [
    path("<int:user>/create/", views.newpost_view, name="newpost"),
    path(
        "<int:photo_pk>/user/<int:author_pk>/delete/",
        views.deletepost_view,
        name="delete",
    ),
    path(
        "<int:photo_pk>/user/<int:author_pk>/edit/",
        views.EditPost.as_view(),
        name="edit",
    ),
    path("<int:photo_pk>/user/<int:user_pk>/like/", views.like_photo, name="like"),
    path(
        "<int:photo_pk>/user/<int:user_pk>/unlike/", views.unlike_photo, name="unlike"
    ),
    path("<int:photo_pk>/likes/", views.LikeList.as_view(), name="likelist"),
    path("search/", views.SearchView.as_view(), name="search"),
    path("<int:pk>/", views.PostDetail.as_view(), name="detail"),
]
