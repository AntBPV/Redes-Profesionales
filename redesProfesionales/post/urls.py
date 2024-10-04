from django.urls import path
from .views import PostApiView

urlpatterns = [
    path('crear-publicacion',PostApiView.as_view()),
    path('list',PostApiView.as_view()),
    path('actualizar-publicacion/<int:pkid>',PostApiView.as_view(),name='actualizar_publicacion')
]
