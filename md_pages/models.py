from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtailmarkdown.fields import MarkdownField


class MdPages(Page):
    # body = MarkdownField()

    # content_panels = [
    #     FieldPanel("title", classname="full title"),
    #     FieldPanel("body"),
    # ]

    body = MarkdownField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]