from django.db import models
from utils.constants import JOURNAL_TYPES
from django.utils import timezone


class BookJournalBase(models.Model):
    name = models.CharField(max_length=255, blank=True, verbose_name='Название')
    price = models.IntegerField(default=0, verbose_name='Цена')
    description = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateField(verbose_name='Дата создания', default=timezone.now())

    class Meta:
        abstract = True


class Book(BookJournalBase):
    num_pages = models.IntegerField(default=0, verbose_name='Количество страниц')
    genre = models.CharField(max_length=255, blank=True, verbose_name='Жанр')


class Journal(BookJournalBase):
    type = models.SmallIntegerField(choices=JOURNAL_TYPES)
    publisher = models.CharField(max_length=255, blank=True, verbose_name='Автор')
