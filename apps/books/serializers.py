from rest_framework import serializers

from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"



class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'pages',
            'author'
        ]


class AuthorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'id'
        ]


class BookCreateSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'pages',
            'author'
        ]

    # def create(self, validated_data):
    #     author_data = validated_data.pop('author')
    #     author = Author.objects.create(**author_data)
    #     book = Book.objects.create(author=author, **validated_data)
    #     return book