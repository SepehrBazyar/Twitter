from django.shortcuts import render
from django.views import View
from .models import Post

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
