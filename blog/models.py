from django import forms
from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet

class BlogPage(Page):

    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]


