from django.db import models
from django.contrib.auth import get_user_model
from shop.escooter.models import EScooter

User = get_user_model()


# Create your models here.

class Cart(models.Model):  # модель корзины товаров
    user = models.ForeignKey(
        User,
        related_name='cart_of_user',
        blank=True,
        null=True,
        on_delete=models.PROTECT)

    created_day = models.DateTimeField(
        "Дата добавления в корзину",
        auto_now=False,
        auto_now_add=True)

    updated_date = models.DateTimeField(
        "Дата последнего изменения",
        auto_now=True,
        auto_now_add=False)

    def __str__(self):
        return "Корзина {} заказчика {}".format(self.pk, self.user)

    @property
    def escooters_in_cart_count(self):  # количество итемов в корзинке
        total = 0
        for product in self.user_cart.all():
            total += product.quantity
        return total

    @property
    def total_cart_price(self):  # цена за них
        total = 0
        for product in self.user_cart.all():
            total += product.price_total
        return total

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class EScooterInCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Корзина', related_name='user_cart')
    escooter = models.ForeignKey(EScooter, on_delete=models.CASCADE, verbose_name='Заказ', related_name='escooter_in_cart')
    quantity = models.PositiveIntegerField("Количество")

    created_day = models.DateTimeField(
        "Дата внесения в корзину",
        auto_now=False,
        auto_now_add=True)

    updated_date = models.DateTimeField(
        "Дата последнего изменения",
        auto_now=True,
        auto_now_add=False)

    def __str__(self):
        return self.escooter.name

    @property
    def price_total(self):
        return self.escooter.price * self.quantity

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        unique_together = [['cart', 'escooter']]
