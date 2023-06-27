from django.urls import path
from .views import UserLoginView

app_name, urlpatterns = "accounts", [
    path('login/', UserLoginView.as_view(), name="login"),
]
