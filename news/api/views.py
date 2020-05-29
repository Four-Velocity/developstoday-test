from rest_framework import generics, views, viewsets
from rest_framework.response import Response

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class Posts(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created')
    serializer_class = PostSerializer


class Comments(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class Upvote(views.APIView):

    def get(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)

        post.upvote()

        return Response({'message': f'Post #{pk} was upvoted'})
