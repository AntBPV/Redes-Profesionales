from django.urls import path
from .views import EnterpriseProfileApiView

urlpatterns = [
    # List will be used for getting a list and posting new objects
    path('list', EnterpriseProfileApiView.as_view()),
    # List/pk will be used for getting a single object, deleting and updating it
    path('list/<int:pk>', EnterpriseProfileApiView.as_view()),
]