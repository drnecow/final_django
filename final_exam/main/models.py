from django.db import models


# Abstract class for Book and Journal.
class BookJournalBase(models.Model):
    name = models.CharField(max_length=300)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=1000)
    created_at = models.DateField()

    class Meta:
        abstract = True


# Book model.
class Book(BookJournalBase):
    num_pages = models.PositiveIntegerField()
    genre = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        db_table = 'books'
        ordering = ['id']

    def __str__(self):
        return f'{self.id}: {self.name}'


# Journal model.
class Journal(BookJournalBase):
    type = models.CharField(max_length=10, choices=((1, 'Bullet'), (2, 'Food'), (3, 'Travel'), (4, 'Sport')))
    publisher = models.TextField(max_length=100)

    class Meta:
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журналы'
        db_table = 'journals'
        ordering = ['id']

    def __str__(self):
        return f'{self.id}: {self.name}'
