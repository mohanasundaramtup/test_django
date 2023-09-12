from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views


urlpatterns=[
    path("",views.home,name="home"),
    path("ticket.html/",views.ticket,name="ticket"),
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),
    path("signup/",views.signup,name="signup"),
]
