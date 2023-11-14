from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets


# ViewSets define the view behavior.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
