from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail import hooks
from . import views
from django.urls import path

# class UserChoiceAdmin(ModelAdmin):
#     model = UserChoice
#     menu_label = 'User Choices'
#     menu_icon = 'pick'  # Change as required, this is just an example icon
#     list_display = ('user', 'question', 'choice')
#     search_fields = ('user__username', 'question__question_text', 'choice__choice_text')

# modeladmin_register(UserChoiceAdmin)

from wagtail.snippets import widgets as wagtailsnippets_widgets

@hooks.register('register_snippet_listing_buttons')
def snippet_listing_buttons(snippet, user, next_url=None):
    question_id = snippet.id

    url = f"/admin/snippets/polls/{question_id}"

    yield wagtailsnippets_widgets.SnippetListingButton(
        'Result',
        url,
        priority=10
    )

@hooks.register('register_admin_urls')
def register_calendar_url():
    return [
        path('snippets/polls/<int:pk>', views.ResultsView.as_view(), name='results'),
    ]
