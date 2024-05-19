from django.urls import path
from .views import BlogListView, BlogDeleteView, BlogUpdateView, BlogCreateView, BlogDetailView, BlogSortMyBlogsView

app_name = 'blogs'

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name='post_delete'),
    path('my_blogs', BlogSortMyBlogsView.as_view(), name='my_blogs')
]
