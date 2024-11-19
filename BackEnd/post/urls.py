from django.urls import path
from .views import PostApiView, PostApiAdminView, PostApiPrivateView

urlpatterns = [
    # List will be used for getting a list and posting new objects
    path('list', PostApiView.as_view(), name='post-list'),
    # List/pk will be used for getting a single object, deleting and updating it
    path('list/<int:pk>', PostApiView.as_view(), name='post-detail'),
    # List-all will be used for getting a list with all objects wether active or not
    path('list-all', PostApiAdminView.as_view()),
    # My-Post will be used for getting personal posts
    path('my-posts', PostApiPrivateView.as_view()),
]
