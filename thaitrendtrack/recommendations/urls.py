from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from .views import movie_detail

urlpatterns = [
    path('preferences/', views.preferences, name='preferences'),
    path('recommend/', views.recommend, name='recommend'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.signup, name='signup'),
    path('homepage/', views.homepage, name='homepage'),
    path('admin/', admin.site.urls),
    path('movies/', views.movies, name='movies'),
    path('movies/<int:movie_id>/', movie_detail, name='movie_detail'),
]

