# Generated by Django 4.0.5 on 2022-06-22 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ferumbel', '0006_alter_order_purchase'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='benefits',
            options={'ordering': ['id'], 'verbose_name': 'Достижение', 'verbose_name_plural': 'Достижения'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='contacts',
            options={'ordering': ['id'], 'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Продавец', 'verbose_name_plural': 'Продавцы'},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['id'], 'verbose_name': 'Картинка', 'verbose_name_plural': 'Картинки'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='photos',
            options={'ordering': ['id'], 'verbose_name': 'Фото', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id'], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Юзер', 'verbose_name_plural': 'Юзеры'},
        ),
        migrations.AlterModelOptions(
            name='purchase',
            options={'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзины'},
        ),
        migrations.AlterModelOptions(
            name='sections',
            options={'ordering': ['id'], 'verbose_name': 'Секция', 'verbose_name_plural': 'Секции'},
        ),
        migrations.AlterModelOptions(
            name='text',
            options={'ordering': ['id'], 'verbose_name': 'Текст', 'verbose_name_plural': 'Тексты'},
        ),
        migrations.AlterModelOptions(
            name='timetable',
            options={'ordering': ['id'], 'verbose_name': 'График работы', 'verbose_name_plural': 'Графики работы'},
        ),
        migrations.AddField(
            model_name='photos',
            name='product',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='ferumbel.product'),
            preserve_default=False,
        ),
    ]
