from rest_framework.serializers import ModelSerializer

from .models import FaultCommentModel, FaultModel


class FaultCommentsSerializer(ModelSerializer):
    class Meta:
        model = FaultCommentModel
        fields = ['id', 'comment_body', 'fault_msg', 'user', 'created_at', 'updated_at']
        read_only_fields = ('user', 'fault_msg')


class FaultSerializer(ModelSerializer):
    comments = FaultCommentsSerializer(many=True, read_only=True)

    class Meta:
        model = FaultModel
        fields = ['id', 'title', 'body', 'problem_solving', 'comments', 'user', 'created_at', 'updated_at']
        read_only_fields = ('user',)
