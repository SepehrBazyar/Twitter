from django.urls import path
from .views import PostView

urlpatterns = [
    path('posts/', PostView.as_view(), name="show_posts"),
]
