from django.db import models
from shopcart.models import Cart
from reference.models import OrderStatus


class Order(models.Model):
    cart = models.ForeignKey(
        Cart,
        related_name="order_cart",
        on_delete=models.PROTECT
    )

    status = models.ForeignKey(
        OrderStatus,
        verbose_name="Статус заказа",
        on_delete=models.PROTECT
    )

    canceled = models.BooleanField(
        "Отменен",
        default=False
    )

    delivery_city = models.CharField(
        "Город",
        null=True,
        blank=True,
        max_length=35
    )

    delivery_street = models.CharField(
        "Улица",
        null=True,
        blank=True,
        max_length=50
    )

    delivery_building = models.CharField(
        "Дом",
        null=True,
        blank=True,
        max_length=5
    )

    delivery_flat = models.CharField(
        "Квартира",
        null=True,
        blank=True,
        max_length=5
    )

    email = models.EmailField(
        verbose_name="Электронная почта",
        null=True,
        blank=True,
        help_text="user@mail.com"
    )

    phone = models.CharField(
        verbose_name="Контактный телефон",
        help_text="+XXX-XX-XXX-XX-XX",
        max_length=17,
    )

    created_day = models.DateTimeField(
        "Дата внесения в корзину",
        auto_now=False,
        auto_now_add=True)

    updated_date = models.DateTimeField(
        "Дата последнего изменения",
        auto_now=True,
        auto_now_add=False)

    def __str__(self):
        return "Заказ № {}".format(self.cart.pk)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
