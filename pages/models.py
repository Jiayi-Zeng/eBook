from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel

class Pages(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        InlinePanel('questions', label="Questions"),
    ]

class BlogPageGalleryImage(Orderable):
    page = ParentalKey(Pages, on_delete=models.CASCADE, related_name='questions')
    
    question = RichTextField(blank=True)
    answer = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('question'),
        FieldPanel('answer'),
    ]