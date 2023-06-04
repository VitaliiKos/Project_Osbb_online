from rest_framework import status
from rest_framework.generics import (
    GenericAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404,
)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .models import FaultCommentModel, FaultModel
from .serializers import FaultCommentsSerializer, FaultSerializer


class FaultListCreateView(ListCreateAPIView):
    queryset = FaultModel.objects.all()
    serializer_class = FaultSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FaultRetrieveView(RetrieveUpdateAPIView):
    queryset = FaultModel.objects.all()
    serializer_class = FaultSerializer
    permission_classes = (IsAuthenticated,)


class FaultCommentListCreateView(ListCreateAPIView):
    queryset = FaultModel.objects.all()
    serializer_class = FaultCommentsSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        fault_id = self.kwargs['pk']
        fault_msg = get_object_or_404(FaultModel, id=fault_id)
        serializer.save(user=self.request.user, fault_msg=fault_msg)

    def get(self, *args, **kwargs):
        fault_msg = self.get_object()
        serializer = self.serializer_class(fault_msg.comments, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class FaultCommentUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    # queryset = FaultCommentModel.objects.all()
    serializer_class = FaultCommentsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return FaultCommentModel.objects.filter(user_id=self.request.user.pk)


class FaultChangeStatusToDoneView(GenericAPIView):
    queryset = FaultModel.objects.all()
    permission_classes = (IsAdminUser,)

    def patch(self, *args, **kwargs):
        fault_msg = self.get_object()
        if fault_msg.problem_solving:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        fault_msg.problem_solving = True
        fault_msg.save()
        serializer = FaultSerializer(fault_msg)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FaultChangeStatusToActiveView(GenericAPIView):
    queryset = FaultModel.objects.all()
    permission_classes = (IsAdminUser,)

    def patch(self, *args, **kwargs):
        fault_msg = self.get_object()
        if not fault_msg.problem_solving:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        fault_msg.problem_solving = False
        fault_msg.save()
        serializer = FaultSerializer(fault_msg)
        return Response(serializer.data, status=status.HTTP_200_OK)
