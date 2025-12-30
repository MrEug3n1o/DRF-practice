from rest_framework import serializers
from borrowing.models import Borrowing
from books.models import Book
from user.models import User
from books.serializers import BookSerializer


class BorrowingSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(
        queryset=Book.objects.all(), slug_field="title"
    )
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="email"
    )

    class Meta:
        model = Borrowing
        fields = (
            "id",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
            "book",
            "user"
        )

    def get_is_active(self, obj):
        return obj.actual_return_date is None


class BorrowingBookDetailSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=False, read_only=True)
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="email"
    )
    class Meta:
        model = Borrowing
        fields = (
            "id",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
            "book",
            "user"
        )


class BorrowingCreateSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(
        queryset=Book.objects.all(), slug_field="title"
    )
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="email"
    )
    class Meta:
        model = Borrowing
        fields = (
            "id",
            "book",
            "expected_return_date",
            "user",
        )

    def validate(self, attrs):
        user = attrs["user"]
        returned_books = Borrowing.objects.filter(user=user, actual_return_date__isnull=True)

        if returned_books.exists():
            raise serializers.ValidationError("RETURN BOOKS")
        return attrs
