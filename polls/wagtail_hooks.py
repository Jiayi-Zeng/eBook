from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail import hooks
from . import views
from django.urls import path
from polls.models import UserChoice


from wagtail.snippets import widgets as wagtailsnippets_widgets

@hooks.register('register_snippet_listing_buttons')
def snippet_listing_buttons(snippet, user, next_url=None):
    question_id = snippet.id

    url = f"/admin/snippets/polls/{question_id}"

    yield wagtailsnippets_widgets.SnippetListingButton(
        'History',
        url,
        priority=15
    )

@hooks.register('register_snippet_listing_buttons')
def snippet_listing_buttons(snippet, user, next_url=None):
    question_id = snippet.id

    url = f"/admin/snippets/polls/publish/{question_id}"

    yield wagtailsnippets_widgets.SnippetListingButton(
        'Publish',
        url,
        priority=10
    )

@hooks.register('register_admin_urls')
def register_calendar_url():
    return [
        path('snippets/polls/<int:pk>', views.ResultsView.as_view(), name='results'),
    ]

@hooks.register('register_admin_urls')
def register_calendar_url():
    return [
        path('snippets/polls/publish/<int:pk>/', views.ResultsView.as_view(), name='results'),
    ]
