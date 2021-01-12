from django.urls import path
from.views import PostListView, PostDetailView, like_view


app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('detail/<slug>', PostDetailView.as_view(), name='detail'),
    path('like/<slug>/', like_view, name='like')
]