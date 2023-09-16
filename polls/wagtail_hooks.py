from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail import hooks
from . import views
from django.urls import path
from polls.models import UserChoice, Publish, Question, PublishQuestionForm
from wagtail.contrib.modeladmin.views import CreateView

from wagtail.snippets import widgets as wagtailsnippets_widgets

@hooks.register('register_snippet_listing_buttons')
def snippet_history_buttons(snippet, user, next_url=None):
    question_id = snippet.id

    url = f"/admin/snippets/polls/{question_id}"

    yield wagtailsnippets_widgets.SnippetListingButton(
        'History',
        url,
        priority=15
    )

@hooks.register('register_snippet_listing_buttons')
def snippet_publish_buttons(snippet, user, next_url=None):
    question_id = snippet.id

    url = f"/admin/snippets/polls/publish/{question_id}"

    yield wagtailsnippets_widgets.SnippetListingButton(
        'Publish',
        url,
        priority=10
    )

@hooks.register('register_admin_urls')
def register_history_url():
    return [
        path('snippets/polls/<int:pk>', views.ResultsView.as_view(), name='history'),
    ]

@hooks.register('register_admin_urls')
def register_publish_url():
    return [
        path('snippets/polls/publish/<int:pk>/', views.PublishView.as_view(), name='publish'),
    ]


