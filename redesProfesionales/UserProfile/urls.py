from django.urls import path
from .views import ProfileApiView

urlpatterns = [
    # List path will be used for getting a list and posting new objects
    path('list', ProfileApiView.as_view()),
    # List/pk will be used for getting a single object, deleting and updating it
    path('list/<int:pk>', ProfileApiView.as_view()),
]
