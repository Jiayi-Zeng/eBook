from .models import MDPages
from .serializers import MDPageSerializer, PageSerializer
from rest_framework import viewsets
from wagtail.models import Page


# ViewSets define the view behavior.
class MDPageViewSet(viewsets.ModelViewSet):
    queryset = MDPages.objects.all()
    serializer_class = MDPageSerializer

class PageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer