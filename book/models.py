from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index

class Book(Page):
    author = models.CharField(blank=True, max_length=20)
    intro = RichTextField(blank=True)
    
    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('author'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('intro'),
    ]