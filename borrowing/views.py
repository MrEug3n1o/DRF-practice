from datetime import datetime

from django.db import transaction
from rest_framework import mixins, status
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
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
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Borrowing.objects.select_related("book", "user")

        is_active = self.request.query_params.get("is_active")
        user_id = self.request.query_params.get("user_id")

        if not user.is_staff:
            queryset = queryset.filter(user=user)
        else:
            if user_id:
                queryset = queryset.filter(user_id=user_id)

        if is_active is not None:
            if is_active.lower() == "true":
                queryset = queryset.filter(actual_return_date__isnull=True)
            elif is_active.lower() == "false":
                queryset = queryset.filter(actual_return_date__isnull=False)

        return queryset.order_by("-borrow_date")

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
                    raise serializers.ValidationError("No books left")
                book.inventory -= 1
                book.save()
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
