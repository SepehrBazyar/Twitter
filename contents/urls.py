from django.urls import path
from .views import PostListView, PostDetailView

app_name, urlpatterns = "contents", [
    path('', PostListView.as_view(), name="home"),
    path('<uuid:id>/', PostDetailView.as_view(), name="detail"),
]
