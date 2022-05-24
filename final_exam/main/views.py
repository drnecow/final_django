import json

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Book, Journal
from .serializers import BookSerializer, JournalSerializer


# CRUD for Book model
class BookViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def get_book(self, book_id):
        return Book.objects.filter(id=book_id).first()

    def create(self, request):
        if not request.user.is_staff:
            return Response({"message": "Access denied."})

        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, book_id):
        book = self.get_book(book_id=book_id)

        if book:
            serializer = BookSerializer(book)
            return Response(serializer.data)
        else:
            return Response({"message": "Book not found."}, status=404)

    def update(self, request, book_id):
        if not request.user.is_staff:
            return Response({"message": "Access denied."})

        book = self.get_book(book_id=book_id)
        if book:
            data = json.loads(request.body)

            book.name = data.get('name', book.name)
            book.price = data.get('price', book.price)
            book.description = data.get('description', book.description)
            book.created_at = data.get('created_at', book.created_at)
            book.num_pages = data.get('num_pages', book.num_pages)
            book.genre = data.get('genre', book.genre)

            book.save()

            serializer = BookSerializer(book)

            return Response(serializer.data)

        else:
            return Response({"message": "Book to update not found."}, status=404)

    def destroy(self, request, book_id):
        if not request.user.is_superuser:
            return Response({"message": "Access denied."})

        book = self.get_book(book_id=book_id)
        if book:
            book.delete()

            return Response({"message": "Book successfully deleted."}, status=204)
        else:
            return Response({"message": "Book to delete not found."}, status=404)


# CRUD for Journal model.
class JournalViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def get_journal(self, journal_id):
        return Journal.objects.filter(id=journal_id).first()

    def create(self, request):
        if not request.user.is_staff:
            return Response({"message": "Access denied."})

        serializer = JournalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, journal_id):
        journal = self.get_journal(journal_id=journal_id)

        if journal:
            serializer = JournalSerializer(journal)
            return Response(serializer.data)
        else:
            return Response({"message": "Journal not found."}, status=404)

    def update(self, request, journal_id):
        if not request.user.is_staff:
            return Response({"message": "Access denied."})

        journal = self.get_journal(journal_id=journal_id)
        if journal:
            data = json.loads(request.body)

            journal.name = data.get('name', journal.name)
            journal.price = data.get('price', journal.price)
            journal.description = data.get('description', journal.description)
            journal.created_at = data.get('created_at', journal.created_at)
            journal.type = data.get('type', journal.type)
            journal.publisher = data.get('publisher', journal.publisher)

            journal.save()

            serializer = JournalSerializer(journal)

            return Response(serializer.data)

        else:
            return Response({"message": "Journal to update not found."}, status=404)

    def destroy(self, request, journal_id):
        if not request.user.is_superuser:
            return Response({"message": "Access denied."})

        journal = self.get_journal(journal_id=journal_id)
        if journal:
            journal.delete()

            return Response({"message": "Journal successfully deleted."}, status=204)
        else:
            return Response({"message": "Journal to delete not found."}, status=404)
