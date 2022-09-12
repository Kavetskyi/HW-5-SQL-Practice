from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from books.models import Book


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'description', 'year']


class BookDetailSerializer(serializers.ModelSerializer):
    authors = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='first_name'
    )

    genre = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Book
        fields = ['title', 'description', 'rating', 'price', 'year', 'authors', 'genre']


class BookRatingSerializer(serializers.Serializer):
    rating = serializers.FloatField()

    def validate_rating(self, value):
        if value > 10 or value < 0:
            raise ValidationError('Enter a value between 0 and 10.')


class BookPriceSerializer(serializers.Serializer):
    price = serializers.FloatField()

    def validate_price(self, value):
        if value < 0:
            raise ValidationError('The price cannot be negative.')
