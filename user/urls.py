from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = "user"
urlpatterns = [
    path('register/',views.register,name = 'register'),
    path('login/',auth_views.LoginView.as_view(template_name = "user/login.html"),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='main:index'),name='logout'),
    path('profile/',views.profile,name = 'profile'),
]
