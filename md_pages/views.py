from .models import MDPages
from .serializers import MDPageSerializer
from rest_framework import viewsets


# ViewSets define the view behavior.
class MDPageViewSet(viewsets.ModelViewSet):
    queryset = MDPages.objects.all()
    serializer_class = MDPageSerializer