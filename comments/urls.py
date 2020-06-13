from django.urls import path
from . import views

app_name = "comments"


urlpatterns = [
    path("photo/<int:photo_pk>/", views.CommentListView.as_view(), name="list"),
    path(
        "photo/<int:photo_pk>/create/",
        views.CreateCommentView.as_view(),
        name="create",
    ),
    path(
        "<int:comment_pk>/photo/<int:photo_pk>/edit/",
        views.EditCommentView.as_view(),
        name="edit",
    ),
    path(
        "<int:comment_pk>/photo/<int:photo_pk>/delete/",
        views.DeleteCommentView.as_view(),
        name="delete",
    ),
]
