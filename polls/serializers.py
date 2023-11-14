from django.urls import path, include
from .models import Question, Publish, UserChoice, Choice
from rest_framework import serializers

# Serializers define the API representation.
class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['question_text', 'published', 'page_id', 'correct_choice_id', 'id', 'body']

class PublishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publish
        fields = ['question_id', 'publish_id', 'status', 'pubished_at']

class UserChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserChoice
        fields = ['id', 'user_id', 'submitted_at', 'publish_id', 'correct', 'choice_id']

class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'choice_text', 'sort_order', 'question_id']
    
