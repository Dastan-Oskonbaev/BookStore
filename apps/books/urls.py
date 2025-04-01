from django.urls import path

from .views import BookListApiView, BookDetailApiView

urlpatterns = [
    path('books', BookListApiView.as_view(), name='book-list-view'),
    path('book/<int:pk>', BookDetailApiView.as_view(), name='book-detail-view')
]