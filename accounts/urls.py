from django.urls import path
from . import views

app_name = "accounts"


urlpatterns = [
    path("<int:user>/", views.user_view, name="user"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("<int:user>/setting/", views.setting_view, name="setting"),
    path("search/", views.SearchView.as_view(), name="search"),
]
