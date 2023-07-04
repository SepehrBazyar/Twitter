from django.shortcuts import render, redirect
from django.views import View
from .models import Post
from .forms import PostUpdateForm

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

    def get(self, request, id):
        post = Post.objects.get(id=id)
        comments = post.comment_set.all()
        return render(
            request,
            "contents/detail.html",
            context={
                "post":post,
                "comments":comments,
            },
        )


class PostUpdateView(View):

    def get(self, request, id):
        post = Post.objects.get(id=id)
        form = PostUpdateForm(instance=post)
        return render(
            request,
            "contents/update.html",
            context={
                "form":form,
            },
        )

    def post(self, request, id):
        post = Post.objects.get(id=id)
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("contents:detail", post.id)

        return render(
            request,
            "contents/update.html",
            context={
                "form":form,
            },
        )
