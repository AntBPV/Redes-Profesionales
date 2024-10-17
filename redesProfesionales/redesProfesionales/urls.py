from django.contrib import admin
from django.urls import path, include

from post import urls as post_urls
from UserProfile import urls as profile_urls
from LoginApi import urls as login_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # post path will be used for all the posts objects
    path('api/post/',include(post_urls)),
    # profile path will be used for all the profiles objects
    path('api/profile/',include(profile_urls)),
    # auth path will be used for the authentication, login and signup of users
    path('api/auth/',include(login_urls)),
]
