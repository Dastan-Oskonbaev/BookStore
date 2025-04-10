import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    min_page = django_filters.NumberFilter(field_name='pages', lookup_expr='gte')
    max_page = django_filters.NumberFilter(field_name='pages', lookup_expr='lte')

    class Meta:
        model = Book
        fields = ['min_page', 'max_page', 'is_active']