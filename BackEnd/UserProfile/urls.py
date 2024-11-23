from django.urls import path
from .views import ProfileApiView, ProfileApiAdminView, ProfileApiPrivateView

urlpatterns = [
    # List path will be used for getting a list and posting new objects
    path('list', ProfileApiView.as_view(), name='profile-list'),
    # List/pk will be used for getting a single object, deleting and updating it
    path('list/<int:pk>', ProfileApiView.as_view(), name='profile-detail'),
    # List-all path will be used for getting a list with all objects wether active or not
    path('list-all', ProfileApiAdminView.as_view()),
    # My-Profile will be used for getting personal profiles
    path('my-profile', ProfileApiPrivateView.as_view()),
]
