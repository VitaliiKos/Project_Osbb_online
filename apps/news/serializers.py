from rest_framework.serializers import ModelSerializer

from .models import CommentsModel, NewsModel


class CommentSerializer(ModelSerializer):
    class Meta:
        model = CommentsModel
        fields = ['id', 'comment_body', 'news', 'user', 'created_at']
        read_only_fields = ('user', 'news')


class NewsSerializer(ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = NewsModel
        fields = ['id', 'title', 'body', 'user', 'comments', 'created_at']
        read_only_fields = ('user',)
