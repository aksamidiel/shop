# Generated by Django 2.2.7 on 2019-12-12 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('escooters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_day', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления в корзину')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cart_of_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
            },
        ),
        migrations.CreateModel(
            name='EScooterInCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('created_day', models.DateTimeField(auto_now_add=True, verbose_name='Дата внесения в корзину')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_cart', to='cart.Cart', verbose_name='Корзина')),
                ('escooter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='escooter_in_cart', to='escooters.EScooter', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'unique_together': {('cart', 'escooter')},
            },
        ),
    ]