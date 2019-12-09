# Generated by Django 2.2.7 on 2019-12-09 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reference', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EScooter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название модели')),
                ('image', models.ImageField(blank=True, null=True, upload_to='scooter_images/', verbose_name='Картинка')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Цена')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание модели')),
                ('year', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Год выпуска')),
                ('identityNum', models.CharField(default='1', max_length=20, unique=True, verbose_name='Идентификационный номер')),
                ('weight', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Вес, гр')),
                ('escooter_amount', models.PositiveIntegerField(default=0, verbose_name='Кол-во скутеров в наличии')),
                ('available', models.BooleanField(default=True, verbose_name='Доступна для заказа')),
                ('rate', models.FloatField(default=0, verbose_name='Рейтинг')),
                ('created_day', models.DateTimeField(auto_now_add=True, verbose_name='Дата внесения в каталог')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')),
                ('manufacturer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='manufacturers', to='reference.Manufacturer', verbose_name='Производитель')),
                ('serie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='books', to='reference.Series', verbose_name='Серия')),
            ],
            options={
                'verbose_name': 'Электро скутер',
                'verbose_name_plural': 'Скутеры',
                'permissions': [('edit_content', 'content manager'), ('edit_order', 'order manager'), ('market', 'for marketers')],
            },
        ),
    ]
