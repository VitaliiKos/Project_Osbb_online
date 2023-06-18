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
    """
    get:
        Get fault list
    post:
        Create fault msg
    """
    queryset = FaultModel.objects.all()
    serializer_class = FaultSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FaultRetrieveView(RetrieveUpdateAPIView):
    """
    get:
        Get fault by id
    patch:
        Partial update fault by id
    put:
        Full update fault by id
    """
    queryset = FaultModel.objects.all()
    serializer_class = FaultSerializer
    permission_classes = (IsAuthenticated,)


class FaultCommentListCreateView(ListCreateAPIView):
    """
    get:
        Get fault's comments
    post:
        Create fault's comment
    """
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
    """
    get:
        Get fault's comment by id
    patch:
        Partial update fault's comment by id
    put:
        Full update fault's comment by id
    delete:
        Delete fault's comment by id
    """
    serializer_class = FaultCommentsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return FaultCommentModel.objects.filter(user_id=self.request.user.pk)


class FaultChangeStatusToDoneView(GenericAPIView):
    """
        Change fault's msg status to done
    """
    queryset = FaultModel.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = FaultSerializer

    def patch(self, *args, **kwargs):
        fault_msg = self.get_object()
        if fault_msg.problem_solving:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        fault_msg.problem_solving = True
        fault_msg.save()
        serializer = FaultSerializer(fault_msg)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FaultChangeStatusToActiveView(GenericAPIView):
    """
    Change fault's msg status to active
    """
    queryset = FaultModel.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = FaultSerializer

    def patch(self, *args, **kwargs):
        fault_msg = self.get_object()
        if not fault_msg.problem_solving:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        fault_msg.problem_solving = False
        fault_msg.save()
        serializer = FaultSerializer(fault_msg)
        return Response(serializer.data, status=status.HTTP_200_OK)
