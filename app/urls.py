from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('token/', views.token, name='token'),
    path('board/', views.board, name='board')

]