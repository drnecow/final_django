from rest_framework.serializers import ModelSerializer
from .models import Book, Journal


# Serializer for Book model.
class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


# Serializer for Journal model.
class JournalSerializer(ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'
