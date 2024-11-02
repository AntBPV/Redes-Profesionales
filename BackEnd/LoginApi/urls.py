from django.urls import path

from .views import signup, login, test_token

urlpatterns = [
    path('signup', signup),
    path('login', login),
    path('test_token', test_token),
]