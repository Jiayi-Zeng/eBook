from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls

from search import views as search_views

from rest_framework import routers, serializers, viewsets

from book.views import BookViewSet
from md_pages.views import MDPageViewSet, PageViewSet
from polls.views import QuestionViewSet, PublishViewSet, ChoiceViewSet, UserChoiceViewSet
from polls_cloze.views import ClozePublishViewSet, ClozeQuestionViewSet, ClozeUserChoiceViewSet
from wagtail.api.v2.router import WagtailAPIRouter

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff', 'is_superuser', 'is_active', 'password', 'last_login', 'last_name', 'first_name', 'date_joined']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'book', BookViewSet)
router.register(r'md_page', MDPageViewSet)
router.register(r'pages', PageViewSet)
router.register(r'question', QuestionViewSet)
router.register(r'publish', PublishViewSet)
router.register(r'choice', ChoiceViewSet)
router.register(r'userchoice', UserChoiceViewSet)
router.register(r'cloze_publish', ClozePublishViewSet)
router.register(r'cloze_question', ClozeQuestionViewSet)
router.register(r'cloze_userchoice', ClozeUserChoiceViewSet)




urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("polls/", include("polls.urls")),
    path("cloze_polls/", include("polls_cloze.urls")),
    path('accounts/', include('allauth.urls')),
    path('chat/', include('chatbot.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    path('', include(wagtail_urls)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


