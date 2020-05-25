from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('post/<int:id>/edit/', views.post_edit, name='post_edit'),
]