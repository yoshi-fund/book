from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'user'


urlpatterns = [
    path('', views.Create.as_view(), name='create'),
    path('thanks/', views.Thanks.as_view(), name='thanks'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout')
]