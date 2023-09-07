from wagtail.admin.panels import FieldPanel
from wagtail.admin.ui.tables import UpdatedAtColumn
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.panels import TabbedInterface, ObjectList


from qa.models import Member, MemberFilterSet


class MemberViewSet(SnippetViewSet):
    model = Member
    icon = "user"
    list_display = ["name", "shirt_size", "get_shirt_size_display", UpdatedAtColumn()]
    list_per_page = 50
    inspect_view_enabled = True
    admin_url_namespace = "member_views"
    base_url_path = "internal/member"
    filterset_class = MemberFilterSet
    # alternatively, you can use the following instead of filterset_class
    # list_filter = ["shirt_size"]
    # or
    # list_filter = {"shirt_size": ["exact"], "name": ["icontains"]}

    edit_handler = TabbedInterface([
        ObjectList([FieldPanel("name")], heading="Details"),
        ObjectList([FieldPanel("shirt_size")], heading="Preferences"),
    ])

register_snippet(MemberViewSet)