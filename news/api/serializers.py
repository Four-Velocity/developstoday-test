from rest_framework import serializers

from .models import Post, Comment


class PostSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="comments-detail",
    )

    class Meta:
        model = Post
        fields = ["id", "title", "link", "created", "upvotes", "author", "comments"]
        read_only_fields = ["upvotes"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "id",
            "post",
            "author",
            "content",
            "created",
        ]
