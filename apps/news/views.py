from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    get_object_or_404,
)
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import CommentsModel, NewsModel
from .serializers import CommentSerializer, NewsSerializer


class NewsListCreateView(CreateAPIView):
    serializer_class = NewsSerializer
    permission_classes = (IsAdminUser,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class NewsListView(ListAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated,)


class NewsRetrieveView(RetrieveAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated,)


class NewsDestroyView(DestroyAPIView):
    queryset = NewsModel.objects.all()
    permission_classes = (IsAdminUser,)

    def destroy(self, request, *args, **kwargs):
        news = self.get_object()
        # user = self.request.user['is_staff']
        # print('#####36######', user)
        # if not self.request.user['is_staff']:
        #     return Response(status=status.HTTP_403_FORBIDDEN)

        self.perform_destroy(news)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentListCreateView(ListCreateAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        news_id = self.kwargs['pk']
        news = get_object_or_404(NewsModel, id=news_id)
        serializer.save(user=self.request.user, news=news)

    def get(self, *args, **kwargs):
        news = self.get_object()
        serializer = self.serializer_class(news.comments, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
