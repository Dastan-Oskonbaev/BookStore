from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.books.models import Book
from apps.books.serializers import BookSerializer


class BookListApiView(APIView):
    def get(self):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailApiView(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return None


    def get(self, request, pk):
        book = self.get_object(pk)
        if book is None:
            return Response('error')
        serializer = BookSerializer(book)
        return Response(serializer.data)




