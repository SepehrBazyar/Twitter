from django.urls import path
from .views import PostListView

app_name, urlpatterns = "contents", [
    path('', PostListView.as_view(), name="home"),
]
