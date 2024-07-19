from django.urls import path

from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('blog_list', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('create', BlogCreateView.as_view(), name='add_blog'),
    path('edit/<int:pk>', BlogUpdateView.as_view(), name='update_blog'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='delete'),
]