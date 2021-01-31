from django.urls import path
from .views import HomeView, PostDetailView, CreatePostView, PostEditView, PostDeleteView
from . import views
urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('article/<int:pk>/',PostDetailView.as_view(),name="post-detail"),
    path('post/new/',CreatePostView.as_view(),name="post-new"),
    path('article/<int:pk>/edit/',PostEditView.as_view(),name="post-edit"),
    path('article/<int:pk>/remove/',PostDeleteView.as_view(),name='post-delete'),
    path('about/', views.about, name='about'),
]