from rest_framework import serializers
from .models import Borrowing

class BorrowingSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="title"
    )
    user = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="email"
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
