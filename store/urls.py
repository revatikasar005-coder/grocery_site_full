from django.urls import path
from . import views

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("home/", views.home, name="home"),
    path("index/", views.home, name="index"),
    path("offers/", views.offers, name="offers"),
    path("deals/", views.deals, name="deals"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("logout/", views.logout_view, name="logout"),
]
