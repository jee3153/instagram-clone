from django.db.models import Q
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views.generic import View
from accounts.models import User
from .models import Chat, Message
from .forms import sendMessage


def create_chat(request, host_pk, guest_pk):
    host = User.objects.get_or_none(pk=host_pk)
    guest = User.objects.get_or_none(pk=guest_pk)
    if host is not None and guest is not None:
        try:
            # user Q() & Q() when filtering twice is needed.
            chat = Chat.objects.get(Q(participants=host) & Q(participants=guest))
        except Chat.DoesNotExist:
            chat = Chat.objects.create()
            chat.participants.add(host, guest)

        return redirect(reverse("chats:detail", kwargs={"pk": chat.pk}))


class ChatDetailView(View):
    def get(self, *args, **kwargs):
        pk = kwargs.get("pk")
        chat = get_object_or_404(Chat, pk=pk)
        context = {"chat": chat}
        return render(self.request, "chats/chat_detail.html", context)

    def post(self, request, *args, **kwargs):
        # print(request.POST)
        message = request.POST.get("message", None)
        pk = kwargs.get("pk")
        chat = get_object_or_404(Chat, pk=pk)
        if message is not None:
            Message.objects.create(user=request.user, message=message, chat=chat)
        return redirect(reverse("chats:detail", kwargs={"pk": pk}))
