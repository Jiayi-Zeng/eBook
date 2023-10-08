import datetime
from django import forms
from django.db import models
from django.utils import timezone
from wagtail.snippets.models import register_snippet
from django.contrib.auth.models import User
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.models import Page, Orderable
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey
from wagtail.snippets.views.snippets import SnippetViewSet
from md_pages.models import MdPages
from wagtail.admin.ui.tables import UpdatedAtColumn


# @register_snippet
class Question(ClusterableModel):
    page = ParentalKey(MdPages, on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length=200)
    published = models.BooleanField(default=False)

    panels = [
        FieldPanel('page'),
        FieldPanel('question_text'),
        InlinePanel('choices', label="Choices"),
    ]

    def __str__(self):
        return self.question_text
    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

class QuestionViewSet(SnippetViewSet):
    model = Question
    icon = "clipboard-list"
    list_display = ['question_text', 'page', 'published', UpdatedAtColumn()]
    list_per_page = 50

register_snippet(QuestionViewSet)

class Choice(Orderable):
    question = ParentalKey(Question, on_delete=models.CASCADE, related_name='choices')
    # question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    
    choice_text = models.CharField(max_length=200)

    panels = [
        FieldPanel('choice_text'),
    ]

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = "Choice"
        verbose_name_plural = "Choices"
    
class Publish(models.Model):
    publish_id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    # pubished_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        # if not self.pk:
        #     max_id = Publish.objects.all().aggregate(max_id=models.Max('publish_id'))['max_id'] or 0
        #     self.publish_id = max_id + 1
        super(Publish, self).save(*args, **kwargs)

class UserChoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True) 
    publish = models.ForeignKey(Publish, on_delete=models.CASCADE)