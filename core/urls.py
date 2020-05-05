from django.urls import path
from photos import views

app_name = "core"

urlpatterns = [
    path("", views.home_view, name="home"),
]
