# Generated by Django 2.2.7 on 2019-12-10 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shopcart', '0001_initial'),
        ('reference', '0002_orderstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('canceled', models.BooleanField(default=False, verbose_name='Отменен')),
                ('delivery_city', models.CharField(blank=True, max_length=35, null=True, verbose_name='Город')),
                ('delivery_street', models.CharField(blank=True, max_length=50, null=True, verbose_name='Улица')),
                ('delivery_building', models.CharField(blank=True, max_length=5, null=True, verbose_name='Дом')),
                ('delivery_flat', models.CharField(blank=True, max_length=5, null=True, verbose_name='Квартира')),
                ('email', models.EmailField(blank=True, help_text='user@mail.com', max_length=254, null=True, verbose_name='Электронная почта')),
                ('phone', models.CharField(help_text='+XXX-XX-XXX-XX-XX', max_length=17, verbose_name='Контактный телефон')),
                ('created_day', models.DateTimeField(auto_now_add=True, verbose_name='Дата внесения в корзину')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orderuser_cart', to='shopcart.Cart')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reference.OrderStatus', verbose_name='Статус заказа')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
