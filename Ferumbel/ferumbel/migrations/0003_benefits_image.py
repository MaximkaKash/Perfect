# Generated by Django 4.0.5 on 2022-06-20 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ferumbel', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Benefits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', verbose_name='Фото')),
                ('value', models.TextField(verbose_name='Значение')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='', verbose_name='Фото')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
