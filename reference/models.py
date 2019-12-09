from django.db import models
from django.urls import reverse


# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField('Название _компании', null=False, blank=False, max_length=20)
    country = models.CharField("Страна", null=True, blank=True, max_length=20, default=' ')

    def __str__(self):  # вывод
        return self.name

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class Series(models.Model):
    name = models.CharField("Название_серии", null=False, blank=False, max_length=20)
    description = models.TextField("Описание", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'

# class OrderStatus(models.Model):
#    status_type = models.CharField("Статус_заказа", max_length=30)
#
#    def __str__(self):
#        return self.status_type
#
#    class Meta:
#        verbose_name = 'Статус'
#        verbose_name_plural = 'Статусы'
