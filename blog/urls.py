# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='blog-list'),
    path('post/<int:pk>/', views.post_detail, name='blog-detail'),
    path('post/new/', views.post_create, name='blog-create'),
    path('post/<int:pk>/edit/', views.post_update, name='blog-update'),
    path('post/<int:pk>/delete/', views.post_delete, name='blog-delete'),
]
