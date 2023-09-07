from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.panels import FieldPanel

from pages.models import MultipleChoice

class AdvertViewSet(SnippetViewSet):
    model = MultipleChoice

    panels = [
        FieldPanel('intro'),
        FieldPanel('question'),
        FieldPanel('answer'),
        FieldPanel('optionA'),
        FieldPanel('optionB'),
        FieldPanel('optionC'),
        FieldPanel('optionD'),
    ]

register_snippet(MultipleChoice)