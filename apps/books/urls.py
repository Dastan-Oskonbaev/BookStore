
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AuthorCreateView, BookViewSet

router = DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    # path('books', BookListApiView.as_view(), name='book-list-view'),
    # path('book/<int:pk>', BookDetailApiView.as_view(), name='book-detail-view')
    # path('list', BookListView.as_view(), name='books-list'),
    # path('detail/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('author-create', AuthorCreateView.as_view(), name='author-create'),
    # path('book-create', BookCreateView.as_view(), name='book-create'),
    path('', include(router.urls)),
]