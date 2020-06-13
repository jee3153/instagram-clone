from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, Http404
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from .models import Comment
from photos.models import Photo
from .forms import CommentForm


class CommentListView(LoginRequiredMixin, TemplateView):
    """ Comment list View """

    login_url = "accounts:login"
    model = Comment
    template_name = "comments/comment_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(photo_id=self.kwargs["photo_pk"])
        return context


class CreateCommentView(LoginRequiredMixin, CreateView):
    """ Creating comment View """

    login_url = "accounts:login"
    form_class = CommentForm
    template_name = "comments/create_comment.html"
    pk_url_kwarg = "photo_pk"

    def get_context_data(self, **kwargs):
        context = super(CreateCommentView, self).get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(photo_id=self.kwargs["photo_pk"])
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        photo = get_object_or_404(Photo, pk=self.kwargs["photo_pk"])
        form.instance.commenter = self.request.user
        self.object.photo = photo
        self.object.save()
        return super(CreateCommentView, self).form_valid(form)


class EditCommentView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """ Editing comment View """

    model = Comment
    form_class = CommentForm
    template_name = "comments/edit_comment.html"
    context_object_name = "comment"
    success_message = "Comment edited"
    pk_url_kwarg = "comment_pk"
    login_url = "accounts:login"

    def get_context_data(self, **kwargs):
        context = super(EditCommentView, self).get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(photo_id=self.kwargs["photo_pk"])
        return context

    def get_object(self, queryset=None):
        comment = super().get_object(queryset)
        if self.request.user.pk != comment.commenter.pk:
            raise Http404()
        return comment


class DeleteCommentView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Comment
    context_object_name = "comment"
    form_class = CommentForm
    success_message = "Comment deleted"
    pk_url_kwarg = "comment_pk"
    login_url = "accounts:login"

    def get_success_url(self):
        photo_pk = self.kwargs.get("photo_pk")
        return reverse_lazy("comments:list", kwargs={"photo_pk": photo_pk})

    def get_object(self, queryset=None):
        comment = super().get_object(queryset)
        user = self.request.user
        commenter = comment.commenter
        post_author = comment.photo.author
        if user.pk is not commenter.pk and user.pk is not post_author.pk:
            raise Http404()
        return comment

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        if request.POST and request.POST.get("yes"):
            self.object.delete()
            messages.success(request, self.success_message)
        return HttpResponseRedirect(success_url)
