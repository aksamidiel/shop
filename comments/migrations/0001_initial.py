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
            name='CommentProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commented_to_order', models.TextField(verbose_name='Комментарий')),
                ('created_day', models.DateTimeField(auto_now_add=True, verbose_name='Дата комментирования')),
                ('commented_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commented_order', to='escooters.EScooter', verbose_name='Заказ с комментом')),
                ('commented_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Коммент',
                'verbose_name_plural': 'Комменты',
            },
        ),
    ]
