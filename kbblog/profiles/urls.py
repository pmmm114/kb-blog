from django.urls import path

from profiles.views import MainViewClass
from profiles.views import PostListView
from profiles.views import PostDetailView
from profiles.views import LogoutView
from profiles.views import PostWriteView
from profiles.views import Loginview

urlpatterns = [
    path('', MainViewClass.as_view(), name='index'),
    path('post', PostListView.as_view(), name='post_list'),
    path('post/<int:post_id>', PostDetailView.as_view(), name='post_detail'),
    path('post/write', PostWriteView.as_view(), name='post_detail'),
    path('logout', LogoutView.as_view(), name='logout_view'),
    path('login', Loginview.as_view(), name='login')
]