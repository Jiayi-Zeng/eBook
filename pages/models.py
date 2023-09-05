from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel

class Pages(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        InlinePanel('multipleChoice', label="MultipleChoice"),
        InlinePanel('clozeQuestion', label="ClozeQuestion"),
    ]

class MultipleChoice(Orderable):
    page = ParentalKey(Pages, on_delete=models.CASCADE, related_name='multipleChoice')
    
    question = RichTextField(blank=True)
    answer = models.CharField(blank=True, max_length=250)
    optionA = models.CharField(blank=True, max_length=250)
    optionB = models.CharField(blank=True, max_length=250)
    optionC = models.CharField(blank=True, max_length=250)
    optionD = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('question'),
        FieldPanel('answer'),
        FieldPanel('optionA'),
        FieldPanel('optionB'),
        FieldPanel('optionC'),
        FieldPanel('optionD'),
    ]

class ClozeQuestion(Orderable):
    page = ParentalKey(Pages, on_delete=models.CASCADE, related_name='clozeQuestion')
    
    question = RichTextField(blank=True)
    answer = models.CharField(blank=True, max_length=250)
    panels = [
        FieldPanel('question'),
        FieldPanel('answer'),
    ]