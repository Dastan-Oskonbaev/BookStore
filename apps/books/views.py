from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from apps.books.filters import BookFilter
from apps.books.models import Book, Author
from apps.books.serializers import BookSerializer, AuthorSerializer, BookCreateSerializer


# class BookListApiView(APIView):
#     def get(self):
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)
#
#
#     def post(self, request, format=None):
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class BookDetailApiView(APIView):
#     def get_object(self, pk):
#         try:
#             return Book.objects.get(pk=pk)
#         except Book.DoesNotExist:
#             return None
#
#
#     def get(self, request, pk):
#         book = self.get_object(pk)
#         if book is None:
#             return Response('error')
#         serializer = BookSerializer(book)
#         return Response(serializer.data)


# class BookListView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     # permission_classes = [IsAuthenticated]
#     # filter_backends = [DjangoFilterBackend]
#     # filterset_fields = ['title', 'pages']
#     filterset_class = BookFilter
#     filter_backends = [SearchFilter, DjangoFilterBackend]
#     search_fields = ['title', 'author__name']


# class BookDetailView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class AuthorCreateView(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# class BookCreateView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookCreateSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer























