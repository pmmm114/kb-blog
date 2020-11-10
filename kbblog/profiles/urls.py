from django.urls import path

from profiles.views import MainViewClass
from profiles.views import PostListView
from profiles.views import PostDetailView

urlpatterns = [
    path('', MainViewClass.as_view(), name='index'),
    path('post', PostListView.as_view(), name='post_list'),
    path('post/<int:post_id>', PostDetailView.as_view(), name='post_detail'),
]