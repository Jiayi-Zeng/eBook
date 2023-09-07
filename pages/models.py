from django.db import models
from django import forms
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.snippets.models import register_snippet

class Pages(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        InlinePanel('multipleChoice', label="MultipleChoice"),
        InlinePanel('clozeQuestion', label="ClozeQuestion"),
    ]

class MultipleChoice(Orderable):
    page = ParentalKey(Pages, on_delete=models.CASCADE, related_name='multipleChoice')
    
    shortcut = models.CharField(blank=False, max_length=250)
    question = RichTextField(blank=False)

    option_a = models.CharField(blank=True, max_length=250)
    option_b = models.CharField(blank=True, max_length=250)
    option_c = models.CharField(blank=True, max_length=250)
    option_d = models.CharField(blank=True, max_length=250)
    
    option = [
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
        ("D", "D"),
    ]
    
    answer = models.CharField(max_length=10, choices=option)
    
    
    # pubilish = 
    # end = 


    panels = [
        MultiFieldPanel([
            FieldPanel('shortcut'),
            FieldPanel('question'),
            FieldPanel('answer'),
            MultiFieldPanel([
                FieldPanel('option_a'),
                FieldPanel('option_b'),
                FieldPanel('option_c'),
                FieldPanel('option_d'),
                ], heading="Options"),
        ], heading="Question Info")
    ]

    def __str__(self):
        return self.shortcut

    class Meta:
        verbose_name_plural = 'MultipleChoice'

@register_snippet
class ClozeQuestion(Orderable):
    page = ParentalKey(Pages, on_delete=models.CASCADE, related_name='clozeQuestion')
    
    question = RichTextField(blank=True)
    answer = models.CharField(blank=True, max_length=250)
    panels = [
        FieldPanel('question'),
        FieldPanel('answer'),
    ]

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = 'ClozeQuestion'
