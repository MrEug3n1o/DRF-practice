from datetime import datetime

from django.db import transaction
from rest_framework import mixins, status
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.response import Response

from borrowing.models import Borrowing

from borrowing.serializers import (
    BorrowingSerializer,
    BorrowingBookDetailSerializer,
    BorrowingCreateSerializer,
)


class BorrowingViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Borrowing.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return BorrowingSerializer
        if self.action == "retrieve":
            return BorrowingBookDetailSerializer
        return BorrowingCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = BorrowingCreateSerializer(data=request.data)

        if serializer.is_valid():
            with transaction.atomic():
                book = serializer.validated_data["book"]
                if book.inventory <= 0:
                    raise serializers.ValidationError()
                book.inventory -= 1
                book.save()
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
