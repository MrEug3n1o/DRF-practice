from datetime import datetime

from rest_framework import mixins
from rest_framework import viewsets

from borrowing.models import Borrowing

from borrowing.serializers import (
    BorrowingSerializer,
)


class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
