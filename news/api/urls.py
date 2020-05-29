from django.urls import path
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'posts', views.Posts, basename="posts")
router.register(r'comments', views.Comments, basename='comments')
urlpatterns = router.urls

urlpatterns += [
    path('posts/<int:pk>/upvote/',
         views.Upvote.as_view(),
         name='Upvote the post'),
]
