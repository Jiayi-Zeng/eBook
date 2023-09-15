import datetime

from django.db import models
from django.utils import timezone
from wagtail.snippets.models import register_snippet
from django.contrib.auth.models import User
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.models import Page, Orderable
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey
from wagtail.contrib.forms.views import SubmissionsListView

@register_snippet
class Question(ClusterableModel):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    published = models.BooleanField(default=False)
    published_end_date = models.DateTimeField(null=True, blank=True)

    panels = [
        FieldPanel('question_text'),
        FieldPanel('pub_date'),
        InlinePanel('choices', label="Choices"),
        
    ]

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

class Choice(Orderable):
    question = ParentalKey(Question, on_delete=models.CASCADE, related_name='choices')
    # question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    panels = [
        FieldPanel('choice_text'),
    ]

    def __str__(self):
        return self.choice_text
    

class UserChoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True) 