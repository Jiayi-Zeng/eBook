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

class ClozeQuestion(ClusterableModel):
    id = models.AutoField(primary_key=True)
    page = ParentalKey(MdPages, on_delete=models.CASCADE, related_name='cloze_questions')
    question_text = models.CharField(max_length=200)
    published = models.BooleanField(default=False)
    correct_choice = models.CharField(max_length=200)

    panels = [
        FieldPanel('page'),
        FieldPanel('question_text'),
        FieldPanel('correct_choice'),  # 添加正确答案字段
    ]

    def __str__(self):
        print(self.id)
        return self.question_text

    
    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

class CLozeQuestionViewSet(SnippetViewSet):
    model = ClozeQuestion
    icon = "clipboard-list"
    list_display = ['question_text', 'page', 'published', UpdatedAtColumn()]
    list_per_page = 50

register_snippet(CLozeQuestionViewSet)

class ClozePublish(models.Model):
    publish_id = models.AutoField(primary_key=True)
    question = models.ForeignKey(ClozeQuestion, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    pubished_at = models.DateTimeField(auto_now_add=True, blank=True)
    
    def save(self, *args, **kwargs):
        # if not self.pk:
        #     max_id = Publish.objects.all().aggregate(max_id=models.Max('publish_id'))['max_id'] or 0
        #     self.publish_id = max_id + 1
        super(ClozePublish, self).save(*args, **kwargs)

class ClozeUserChoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    submitted_at = models.DateTimeField(auto_now_add=True) 
    publish = models.ForeignKey(ClozePublish, on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)