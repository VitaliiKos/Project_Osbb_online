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
    """
        List of poll
    """
    queryset = PollModel.objects.filter(visible=True)
    serializer_class = PollSerializer
    permission_classes = (IsAuthenticated,)


class PollCreateView(CreateAPIView):
    """
        Create new poll
    """
    serializer_class = PollSerializer
    permission_classes = (IsAdminUser,)


class PollRetrieveView(RetrieveAPIView):
    """
        Get poll by id
    """
    queryset = PollModel.objects.all()
    serializer_class = PollSerializer
    permission_classes = (IsAuthenticated,)


class PollDestroyView(DestroyAPIView):
    """
        Destroy poll by id
    """
    queryset = PollModel.objects.all()
    permission_classes = (IsAdminUser,)

    def destroy(self, request, *args, **kwargs):
        poll = self.get_object()
        self.perform_destroy(poll)
        return Response(status=status.HTTP_204_NO_CONTENT)


class PollCreateListVoteView(ListCreateAPIView):
    """
    get:
        List of votes
    post:
        Add vote
    """
    queryset = PollModel.objects.all()
    serializer_class = VoteSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        poll_id = self.kwargs['pk']
        poll = get_object_or_404(PollModel, id=poll_id)
        user = self.request.user
        user_vote_status = VoteModel.objects.filter(user_id=user.id, poll_id=poll_id)
        if user_vote_status:
            return Response("You have already voted ")
        choices_data = self.request.data.get('choice')
        get_object_or_404(PollModel, id=poll_id)
        choice = get_object_or_404(ChoiceModel, id=choices_data, poll_id=poll_id)
        serializer.save(user=self.request.user, poll=poll, choice=choice)
