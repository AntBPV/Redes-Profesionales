from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from post import urls as post_urls
from UserProfile import urls as profile_urls
from LoginApi import urls as login_urls
from EnterpriseProfile import urls as enterprise_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # post path will be used for all the posts objects
    path('api/post/',include(post_urls)),
    # profile path will be used for all the profiles objects
    path('api/profile/',include(profile_urls)),
    # e-profile path will be used for all the enterprise profiles objects
    path('api/e-profile/', include(enterprise_urls)),
    # auth path will be used for the authentication, login and signup of users
    path('api/auth/',include(login_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
