from django.urls import path
from .views import PostApiView

urlpatterns = [
    # List will be used for getting a list and posting new objects
    path('list', PostApiView.as_view()),
    # List/pk will be used for getting a single object, deleting and updating it
    path('list/<int:pk>', PostApiView.as_view()),
]
