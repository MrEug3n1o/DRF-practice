from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny

from .models import Book
from .serializers import BookSerializer
from .permissions import IsAdminOrIfAuthenticatedReadOnly

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)
