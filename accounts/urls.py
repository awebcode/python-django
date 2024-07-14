# myproject/urls.py
from django.urls import path
from .views import register, user_info, user_login, test, practice, search_books
urlpatterns = [
    path('register', register, name='register'),
    path('login', user_login, name='login'),
    path('profile', user_info, name='profile'),
    path('test/<str:username>/', test, name='goods'),
    path("query", search_books, name="query"),
    path("practice", practice, name="practice"),
]
