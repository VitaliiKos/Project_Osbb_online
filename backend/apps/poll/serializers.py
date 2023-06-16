from django.db import transaction

from rest_framework.serializers import ModelSerializer, RelatedField, SerializerMethodField

from core.dataclasses.choice_dataclass import Choice

from .models import ChoiceModel, PollModel, VoteModel


class ChoiceRelatedFieldSerializer(RelatedField):

    def to_representation(self, value: Choice):
        return {'id': value.id}


class ChoiceSerializer(ModelSerializer):
    percent = SerializerMethodField()

    class Meta:
        model = ChoiceModel
        fields = ['id', 'percent', 'choice_text']

    def get_percent(self, obj):
        total = VoteModel.objects.filter(poll=obj.poll).count()
        current = VoteModel.objects.filter(poll=obj.poll, choice=obj).count()
        print(current)

        if total != 0:
            return float(current * 100 / total)
        else:
            return float(0)


class PollSerializer(ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = PollModel
        fields = ['id', 'question', 'description', 'choices', 'created_at']

    @transaction.atomic
    def create(self, validated_data: dict):
        choices_data = validated_data.pop('choices', [])
        poll = PollModel.objects.create(**validated_data)
        [ChoiceModel.objects.create(**item, poll=poll) for item in choices_data]
        return poll


class VoteSerializer(ModelSerializer):

    class Meta:
        model = VoteModel
        fields = ('id', 'user', 'poll', 'choice', 'created_at')
        read_only_fields = ('poll', 'user')
