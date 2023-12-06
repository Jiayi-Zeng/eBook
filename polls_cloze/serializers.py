from django.urls import path, include
from .models import ClozeQuestion, ClozePublish, ClozeUserChoice
from rest_framework import serializers

# Serializers define the API representation.
class ClozeQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClozeQuestion
        fields = ['question_text', 'published', 'page_id', 'correct', 'id', 'body']

class ClozePublishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClozePublish
        fields = ['question_id', 'publish_id', 'status', 'pubished_at']

class ClozeUserChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClozeUserChoice
        fields = ['id', 'user_id', 'submitted_at', 'publish_id', 'correct', 'answer']


