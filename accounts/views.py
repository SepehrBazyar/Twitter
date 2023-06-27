from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

# Create your views here.
class UserLoginView(View):

    my_form = LoginForm
    my_template = "accounts/login.html"

    def get(self, request):
        form = self.my_form()
        return render(
            request,
            self.my_template,
            context={
                "form": form,
            },
        )

    def post(self, request):
        form = self.my_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd["name"],
                password=cd["password"],
            )
            if user:
                login(request, user)
                return redirect("contents:home")

        return render(
            request,
            self.my_template,
            context={
                "form": form,
            },
        )
