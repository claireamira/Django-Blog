from django.urls import path
from . import views
from .views import CreatePostView, PostDeleteView 

urlpatterns = [
  path('', views.home, name='blog-home'),
  path("about/", views.about, name='blog-about'),
  path("my-posts/", views.myPosts, name='my-posts'),
  path("contacts/", views.contacts, name='blog-contacts'),
  path("post/<int:pk>/", views.post_detail, name='post-detail'),
  path("post/create/", CreatePostView.as_view(), name='create-post'),  
  path("post/update/<int:pk>", views.PostUpdateView.as_view(), name='post-update'), 
  path("post/delete/<int:pk>", views.PostDeleteView.as_view(), name='post-delete') 
]
  
