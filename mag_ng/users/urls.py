from django.urls import path, include
from django.contrib.auth import views as auth_views
<<<<<<< HEAD

from . import views

=======

from mag_ng.users import views

>>>>>>> 4c6ca556084101156671afc9edae4620a6d344e9
app_name = 'users'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='users/password-change.html'),'name=password-change'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='users/password-reset.html'),name='password-reset'),
    path('profile/<int:pk>/<slug:user>/', views.Profile.as_view(), name='profile'),
]