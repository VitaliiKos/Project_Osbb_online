from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404,
)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .models import CommentsModel, NewsModel
from .serializers import NewsCommentSerializer, NewsSerializer


class NewsListView(ListAPIView):
    """
        List of news
    """
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated,)


class NewsCreateView(CreateAPIView):
    """
        Create news
    """
    serializer_class = NewsSerializer
    permission_classes = (IsAdminUser,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class NewsRetrieveView(RetrieveAPIView):
    """
        Get news by id
    """
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated,)


class NewsDestroyView(DestroyAPIView):
    """
    Destroy news by id
    """
    queryset = NewsModel.objects.all()
    permission_classes = (IsAdminUser,)

    def destroy(self, request, *args, **kwargs):
        news = self.get_object()
        self.perform_destroy(news)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentListCreateView(ListCreateAPIView):
    """
        get:
            List of comments for news
        post:
            Add comment for news
    """
    queryset = NewsModel.objects.all()
    serializer_class = NewsCommentSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        news_id = self.kwargs['pk']
        news = get_object_or_404(NewsModel, id=news_id)
        serializer.save(user=self.request.user, news=news)

    def get(self, *args, **kwargs):
        news = self.get_object()
        serializer = self.serializer_class(news.comments, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class CommentDestroyView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Get comment by id
    patch:
        Partial update comment by id
    put:
        Full update comment by id
    delete:
        Delete comment by id
    """
    serializer_class = NewsCommentSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return CommentsModel.objects.filter(user_id=self.request.user.pk)
