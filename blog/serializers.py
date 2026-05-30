from rest_framework import serializers
from .models import Blog, Comment


class CommentSerializer(serializers.ModelSerializer):
    blog_id = serializers.IntegerField(source='blog.id', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'blog_id', 'comment', 'created_at']


class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'body', 'created_at']


class BlogDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'body', 'created_at', 'comments']
