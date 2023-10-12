from wagtail.models import Page
from wagtail.admin.panels import FieldPanel,InlinePanel
from wagtailmarkdown.fields import MarkdownField
from modelcluster.fields import ParentalKey


class MdPages(Page):


    body = MarkdownField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', icon="code"),
        InlinePanel('questions', label='Question'),
        # InlinePanel('cloze_questions', label='Cloze Question'),
    ]