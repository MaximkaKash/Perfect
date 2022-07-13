from django.conf import settings
from django.db import models
from django.core.mail import send_mail
from django.utils.translation import gettext as _
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import User


class Text(models.Model):
    value = models.TextField(verbose_name="Текст")

    def __str__(self):
        return f"{self.value}"

    class Meta:
        ordering = ["id"]
        verbose_name = _("Text")
        verbose_name_plural = _("Texts")


class Image(models.Model):
    Image = models.ImageField(verbose_name="Фото")

    def __str__(self):
        return f"{self.Image}"

    class Meta:
        ordering = ["id"]
        verbose_name = _("Image")
        verbose_name_plural = _("Images")


class Benefits(models.Model):
    photo = models.ImageField(verbose_name="Фото")
    value = models.TextField(verbose_name="Значение")

    def __str__(self):
        return f"{self.value}"

    class Meta:
        ordering = ["id"]
        verbose_name = _("Benefict")
        verbose_name_plural = _("Benefits")


class Contacts(models.Model):
    pole = models.TextField(null=True, verbose_name="Поле")
    value = models.CharField(max_length=40, null=True, verbose_name="Значение")
    adr = models.URLField(blank=True, null=True, verbose_name="Ссылка")

    def __str__(self):
        return f"{self.pole}"

    class Meta:
        ordering = ["id"]
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")


class Timetable(models.Model):
    name = models.CharField(max_length=200, verbose_name="День недели")
    value = models.TextField(blank=True, null=True, verbose_name="Значение")
    position = models.IntegerField(blank=True, null=True, verbose_name="Позиция")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["id"]
        verbose_name = _("Timetable")
        verbose_name_plural = _("Timetables")


class Category(models.Model):
    Text = models.TextField(blank=True, verbose_name="Название")
    Photo = models.ImageField(blank=True, verbose_name="Фотография")
    is_main = models.BooleanField(default=True, verbose_name="Главная")

    def __str__(self):
        return f"{self.Text}"

    class Meta:
        ordering = ["id"]
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Product(models.Model):
    coast = models.FloatField(default=0, verbose_name="Цена")
    name = models.TextField(max_length=1000, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    popular = models.FloatField(default=0, verbose_name="Популярность")
    Image = models.ImageField(verbose_name="Фотография")
    division = models.BooleanField(blank=True, null=True, verbose_name="Разделение", default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Категория")

    def __str__(self):
        return f"{self.name},{self.coast},{self.description},{self.popular}, {self.category}"

    class Meta:
        ordering = ["id"]
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class Photos(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Картинки")
    photo = models.ImageField(null=True, blank=True, verbose_name="Фото")

    def __str__(self):
        return f"{self.photo}"

    class Meta:
        ordering = ["id"]
        verbose_name = _("Photo")
        verbose_name_plural = _("Photos")


class Sections(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    isMain = models.BooleanField(verbose_name="Главная")
    products = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["id"]
        verbose_name = _("Selection")
        verbose_name_plural = _("Selections")


class Purchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(
        Product, related_name="purchases", on_delete=models.CASCADE, verbose_name='Продукт'
    )
    count = models.IntegerField(verbose_name='Количество')
    index = models.IntegerField(blank=True, null=True, default=1, verbose_name='Индекс пользователя')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата')

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = _("Purchase")
        verbose_name_plural = _("Purchases")


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Продавец')
    index = models.IntegerField(blank=True, null=True, verbose_name='Индекс продавца')
    delivery = models.BooleanField(default=True, null=True, blank=True, verbose_name='Доставка')
    foruser = models.IntegerField(blank=True, null=True, default=None, verbose_name='Связь с пользователем')

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")


class Profile(models.Model):
    name = models.TextField(blank=True, null=True, verbose_name='Имя пользователя')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    phone = models.CharField(max_length=30, blank=True, null=True, verbose_name='Номер телефона')
    email = models.EmailField(blank=True, null=True, verbose_name='Почта')
    adress = models.TextField(blank=True, null=True, verbose_name='Адрес')
    comment = models.TextField(blank=True, null=True, verbose_name='Комментарий к заказу')
    index = models.IntegerField(blank=True, null=True, default=1, verbose_name='Индекс')
    seller = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Продавец')
    delivery = models.BooleanField(blank=True, null=True, verbose_name="Доставка")
    code = models.CharField(max_length=4, blank=True, null=True, verbose_name='Код')

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,
                             verbose_name='Пользователь')
    name = models.TextField(blank=True, null=True, verbose_name='Имя пользователя')
    purchase = models.ForeignKey(
        Purchase, on_delete=models.CASCADE, verbose_name=' Корзина'
    )
    coast = models.IntegerField(blank=True, null=True, default=1, verbose_name='Цена')
    phone = models.CharField(max_length=30, blank=True, null=True, verbose_name='Номер телефона')
    comment = models.TextField(blank=True, null=True, verbose_name='Комментарий')
    delivery = models.BooleanField(blank=True, null=True, verbose_name='Необходима ли доставка')
    adress = models.TextField(blank=True, null=True, verbose_name='Адрес доставки')
    index = models.IntegerField(blank=True, null=True, verbose_name='Индекс покупателя')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, blank=True, null=True, verbose_name='Дата')
    statuc = models.IntegerField(blank=True, null=True, default=1, verbose_name='Статус')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Продавец')

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
