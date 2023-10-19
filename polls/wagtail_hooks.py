from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail import hooks
from . import views
from django.urls import path
from .models import Question
from wagtail.contrib.modeladmin.views import CreateView
from django.shortcuts import get_object_or_404
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register


from wagtail.snippets import widgets as wagtailsnippets_widgets

@hooks.register('register_snippet_listing_buttons')
def snippet_history_buttons(snippet, user, next_url=None):
    question_id = snippet.id
    is_published = snippet.published

    if type(snippet) == Question:
        yield wagtailsnippets_widgets.SnippetListingButton(
            '结果',
            f"/admin/snippets/polls/{question_id}/",
            priority=15
        )

        if is_published:
            button_text = '结束'
            url = f"/admin/snippets/polls/end/{question_id}/"
        else:
            button_text = '发布'
            url = f"/admin/snippets/polls/publish/{question_id}/"

        yield wagtailsnippets_widgets.SnippetListingButton(
            button_text,
            url,
            priority=10
        )

@hooks.register('register_admin_urls')
def register_publish_url():
    return [
        path('snippets/polls/publish/<int:pk>/', views.publish, name='publish'),
        path('snippets/polls/end/<int:pk>/', views.unpublish, name='end'),
        path('snippets/polls/<int:pk>/', views.ResultsView.as_view(), name='history'),
    ]
                
register_snippet(Question)
