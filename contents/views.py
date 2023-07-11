from typing import Any
from django import http
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views import View
from .models import Post
from .forms import PostUpdateForm, CommentForm

# Create your views here.
class PostListView(View):

    def get(self, request):
        print(request.user)
        posts = Post.objects.all()
        return render(
            request,
            "contents/index.html",
            context={
                "posts":posts,
            },
        )


class PostDetailView(View):

    comment_form = CommentForm

    def setup(self, request, id):
        self.this_post = get_object_or_404(Post, id=id)
        return super().setup(request, id)

    def get(self, request, id):
        comments = self.this_post.comment_set.all()
        return render(
            request,
            "contents/detail.html",
            context={
                "post":self.this_post,
                "comments":comments,
                "comment_form": self.comment_form(),
            },
        )

    def post(self, request, id):
        form = self.comment_form(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user, comment.post = request.user, self.this_post
            comment.save()

        return redirect("contents:detail", id)


class PostUpdateView(View):

    def setup(self, request, id):
        self.this_post = get_object_or_404(Post, id=id)
        return super().setup(request, id)

    def dispatch(self, request, id):
        print(request.user.id)
        if self.this_post.user.id != request.user.id:
            return redirect("contents:home")

        return super().dispatch(request, id)

    def get(self, request, id):
        form = PostUpdateForm(instance=self.this_post)
        return render(
            request,
            "contents/update.html",
            context={
                "form":form,
            },
        )

    def post(self, request, id):
        form = PostUpdateForm(
            request.POST,
            request.FILES,
            instance=self.this_post,
        )
        if form.is_valid():
            form.save()
            return redirect("contents:detail", self.this_post.id)

        return render(
            request,
            "contents/update.html",
            context={
                "form":form,
            },
        )
