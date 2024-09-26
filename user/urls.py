from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name= "login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view() , name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name="password_change.html"), name='password_change'),
] 