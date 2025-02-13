from django.db import models

class Book(models.Model):
    casa = models.CharField(max_length=255)
    edicao = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    isbn_number = models.CharField(max_length=13)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.name