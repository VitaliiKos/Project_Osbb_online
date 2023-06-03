from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    get_object_or_404,
)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from apps.poll.models import ChoiceModel, PollModel, VoteModel
from apps.poll.serializers import PollSerializer, VoteSerializer


class PollListView(ListAPIView):
    queryset = PollModel.objects.all()
    serializer_class = PollSerializer
    permission_classes = (IsAuthenticated,)


class PollCreateView(CreateAPIView):
    serializer_class = PollSerializer
    permission_classes = (IsAdminUser,)


class PollRetrieveView(RetrieveAPIView):
    queryset = PollModel.objects.all()
    serializer_class = PollSerializer
    permission_classes = (IsAuthenticated,)


class PollDestroyView(DestroyAPIView):
    queryset = PollModel.objects.all()
    permission_classes = (IsAdminUser,)

    def destroy(self, request, *args, **kwargs):
        poll = self.get_object()
        if not poll.user['is_staff']:
            return Response(status=status.HTTP_403_FORBIDDEN)

        self.perform_destroy(poll)
        return Response(status=status.HTTP_204_NO_CONTENT)


class PollCreateListVoteView(ListCreateAPIView):
    """
    List of votes
    """
    queryset = VoteModel.objects.all()
    serializer_class = VoteSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        poll_id = self.kwargs['pk']
        data = self.request.data
        poll = get_object_or_404(PollModel, id=poll_id)

        choices_data = self.request.data.get('choice')
        get_object_or_404(PollModel, id=poll_id)
        choice = get_object_or_404(ChoiceModel, id=choices_data, poll_id=poll_id)
        print('!!!!!63!!!!!!!',choice)
        # choice = ChoiceModel.objects.get(id=choices_data)
        serializer.save(user=self.request.user, poll=poll, choice=choice)


    # def get_queryset(self):
    #     return VoteModel.objects.filter(user=self.request.user)
    #
    # def perform_create(self, serializer):
    #     poll_id = self.kwargs['pk']
    #     poll = PollModel.objects.get(id=poll_id)
    #     choices_data = self.request.data.get('choice')
    #     user = self.request.user
    #
    #     choice = ChoiceModel.objects.get(id=choices_data)
    #     VoteModel.objects.create(user=user, poll=poll, choice=choice)
    #
    # def create(self, request, *args, **kwargs):
    #     poll_id = kwargs.get('pk')
    #     get_object_or_404(PollModel, id=poll_id)
    #
    #     return super().create(request, *args, **kwargs)
