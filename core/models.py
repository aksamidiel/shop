from django.db import models
from django.urls import reverse
import os


# Create your models here.

class Category(models.Model):  # категория товара
    name = models.CharField("Название_товара",
                            null=False,
                            blank=False,
                            max_length=150,
                            db_index=True)
    slug = models.SlugField(max_length=150,
                            unique=True,
                            db_index=True)
    picture = models.ImageField("Картинка_товара",
                                upload_to='item_images/',
                                null=True,
                                blank=True)
    description = models.TextField("Описание_категории",
                                   blank=True,
                                   null=True)
    created_date_at = models.DateTimeField(auto_now=False,    # дата добавления в каталог
                                           auto_now_add=True)

    updated_date_at = models.DateTimeField(auto_now=True,   # дата последнего апдейта
                                           auto_now_add=False)

    class Meta:
        ordering = ('name',)
        verbose_name = 'категория_товара'
        verbose_name_plural = 'категории_товаров'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):   # модель определенного товара
    category = models.ForeignKey(
        Category, related_name='products',
        on_delete=models.CASCADE
    )
    name = models.CharField("Название_продукта", max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField("Краткое описание", blank=True)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    available = models.BooleanField("Доступность на складе", default=True)
    stock = models.PositiveIntegerField()  # количество на складе
    created_date_at = models.DateTimeField("Товар создан",
                                           auto_now_add=True,
                                           auto_now=False)

    updated_date_at = models.DateTimeField("Товар обновлен",
                                           auto_now_add=False,
                                           auto_now=True)
    image = models.ImageField("Картинка_продукта",
                              upload_to=get_upload_path,
                              blank=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
