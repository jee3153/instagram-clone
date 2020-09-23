from django.urls import path
from . import views

app_name = "chats"

urlpatterns = [
    path("go/<int:host_pk>/<int:guest_pk>/", views.create_chat, name="go"),
    path("<int:pk>/", views.ChatDetailView.as_view(), name="detail"),
]
