
from django.urls import path
from . import views
urlpatterns = [
    path('', views.helloBlog),
     path('about', views.aboutPage),
]
