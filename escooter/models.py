from django.db import models


# Create your models here.

class EScooter(models.Model):
    name = models.CharField(
        "Название модели",
        null=False,
        blank=False,
        max_length=200)

    image = models.ImageField(
        "Картинка",
        upload_to='scooter_images/',
        null=True,
        blank=True)

    price = models.DecimalField(
        "Цена",
        max_digits=5,
        decimal_places=2)

    serie = models.ForeignKey(
        "reference.Series",
        related_name="books",
        verbose_name="Серия",
        null=True,
        blank=True,
        on_delete=models.PROTECT)

    description = models.TextField(
        "Описание модели",
        blank=True,
        null=True
    )

    year = models.PositiveSmallIntegerField(
        "Год выпуска",
        null=True,
        blank=True)

    manufacturer = models.ForeignKey(
        "reference.Manufacturer",
        related_name="manufacturers",
        verbose_name="Производитель",
        null=True,
        blank=True,
        on_delete=models.PROTECT)

    identityNum = models.CharField(
        "Идентификационный номер",
        default="1",
        unique=True,
        max_length=20)

    weight = models.PositiveSmallIntegerField(
        "Вес, гр",
        null=True,
        blank=True, )

    escooter_amount = models.PositiveIntegerField(
        "Кол-во скутеров в наличии",
        default=0)

    available = models.BooleanField(
        "Доступна для заказа",
        default=True)

    rate = models.FloatField(
        "Рейтинг",
        default=0)

    created_day = models.DateTimeField(
        "Дата внесения в каталог",
        auto_now=False,
        auto_now_add=True)

    updated_date = models.DateTimeField(
        "Дата последнего изменения",
        auto_now=True,
        auto_now_add=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Электро скутер'
        verbose_name_plural = 'Скутеры'
        permissions = [('edit_content', 'content manager'), ('edit_order', 'order manager'),  # разрешения на редакцию
                       ('market', 'for marketers')]
