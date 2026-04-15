from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginView(View):
    def get(self, request):
        return render(request, "users/login.html")

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)
            return redirect("home")

        return render(request, "users/login.html", {"error": "Invalid credentials"})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")


class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "users/home.html")
