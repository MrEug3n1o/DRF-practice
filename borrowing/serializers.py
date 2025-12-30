from rest_framework import serializers
from borrowing.models import Borrowing
from books.models import Book
from user.models import User


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
