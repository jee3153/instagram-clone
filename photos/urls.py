from django.urls import path
from . import views

app_name = "photos"


urlpatterns = [
    path("<int:user>/", views.user_view, name="user"),
    path("<int:user>/create/", views.create_view, name="create"),
    path("<int:user>/<int:photo>/edit/", views.edit_view, name="edit"),
]
