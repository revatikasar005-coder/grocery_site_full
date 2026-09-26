from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Product, Category   # Category bhi import kiya

# Welcome Page
def welcome(request):
    return render(request, "welcome.html")

# Signup Page
def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect("home")
    return render(request, "signup.html")

# Login Page
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password!")
    return render(request, "login.html")

# Logout
def logout_view(request):
    logout(request)
    return redirect("login")

# Home / Index Page
def home(request):
    # Saare products fetch karenge
    products = Product.objects.all()
    # Saari categories fetch karenge
    categories = Category.objects.all()

    return render(request, "index.html", {
        "products": products,
        "categories": categories
    })

# Offers Page
def offers(request):
    return render(request, "offers.html")

# Deals Page
def deals(request):
    return render(request, "deals.html")

# Contact Page
def contact(request):
    return render(request, "contact.html")

# About Page
def about(request):
    return render(request, "about.html")
