from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from books.models import Book
from books.serializers import BookListSerializer, BookDetailSerializer, BookRatingSerializer, BookPriceSerializer


# class BookView(APIView):
#     def get(self, request):
#         books = Book.objects.all()
#         serializer = BookListSerializer(books, many=True)
#         return Response({'response': [serializer.data]})


class BookViewSet(ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]
    filterset_fields = ['authors', 'genre']

    def get_serializer_class(self):
        if self.action == 'rate':
            return BookRatingSerializer
        if self.action == 'price':
            return BookPriceSerializer
        if self.action == 'retrieve':
            return BookDetailSerializer
        return BookListSerializer

    @action(detail=True, methods=['POST'])
    def rate(self, request, pk):
        book = Book.objects.get(id=pk)
        rating = float(request.POST.get('rating'))
        serializer = self.get_serializer_class()(data={'rating': rating})
        serializer.is_valid(raise_exception=True)
        print(book.rating)
        if book.rating is None:
            book.rating = rating
        else:
            book.rating = (book.rating + rating) / 2
        book.save()
        return Response({"R": "OK"})

    @action(detail=False)
    def avg_rate(self, request):
        books = Book.objects.all()
        rating_books = sum([book.rating for book in books])
        total_count = books.count()
        return Response({"avg_rating": rating_books / total_count})

    @action(detail=True, methods=['POST'])
    def price(self, request, pk):
        book = Book.objects.get(id=pk)
        price = float(request.POST.get('price'))
        serializer = self.get_serializer_class()(data={'price': price})
        serializer.is_valid(raise_exception=True)
        book.price = price
        book.save()
        return Response({"R": "OK"})

    @action(detail=False)
    def max_min_price(self, request):
        books = Book.objects.all()
        book_with_max_price = max([book.price for book in books])
        book_with_min_price = min([book.price for book in books])
        return Response({"max_price": book_with_max_price, "min_price": book_with_min_price})
