from django.db import models
from cart.models import User


# Create your models here.

class CommentProduct(models.Model):
    commented_order = models.ForeignKey(
        'escooters.EScooter',
        related_name='commented_order',
        verbose_name='Заказ с комментом',
        on_delete=models.CASCADE
    )

    commented_to_order = models.TextField('Комментарий')

    commented_user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    created_day = models.DateTimeField(
        'Дата комментирования',
        auto_now=False,
        auto_now_add=True
    )

    def __str__(self):
        return 'коммент заказчика {} о товаре {}'.format(self.comm)

    class Meta:
        verbose_name = 'Коммент'
        verbose_name_plural = 'Комменты'

