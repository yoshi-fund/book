from django.urls import path
from . import views


app_name = 'book'


urlpatterns = [
    path('', views.List.as_view(), name='list'),
    path('detail/<int:pk>/', views.Detail.as_view(), name='detail'),
    path('create/', views.Create.as_view(), name='create'),
    path('update/<int:pk>/', views.Update.as_view(), name='update'),
    path('delete/<int:pk>/', views.Delete.as_view(), name='delete'),
    path('user_list/<int:user>/', views.UserView.as_view(), name='user_list'),
    path('mypage/', views.Mypage.as_view(), name='mypage'),

  
    
]