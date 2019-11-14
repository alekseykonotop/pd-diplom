from django.db import models
from django.urls import reverse
from datetime import datetime
from os.path import splitext
from django.core import validators
from django.contrib.auth import get_user_model

User = get_user_model()


# Функция для добавляения пути для сохрания файла поля price модели Shop
def get_timestamp_path(instance, filename):
    return f'stores/prices/{instance.trademark_name}/{datetime.now().timestamp()}{splitext(filename)[1]}'


class Shop(models.Model):
    official_name = models.CharField(max_length=50, verbose_name='Наименование организации', blank=True)
    trademark_name = models.CharField(max_length=50, verbose_name='Торговое название')
    slug = models.SlugField(max_length=200, db_index=True)
    url = models.URLField(verbose_name='Ссылка', null=True, blank=True)
    user = models.OneToOneField(User, verbose_name='Пользователь',
                                blank=True, null=True,
                                on_delete=models.CASCADE)
    state = models.BooleanField(verbose_name='статус получения заказов', default=True)

    price = models.FileField(max_length=200, verbose_name='Прайс-лист',
                             upload_to=get_timestamp_path,
                             validators=[validators.FileExtensionValidator(
                                 allowed_extensions=('csv', ))],
                             error_messages={'invalid_extension': 'Этот формат не поддерживается. '
                                                                  'Загрузите файл с расширением .csv'}, blank=True)

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = "Список магазинов"
        ordering = ('-trademark_name',)

    def __str__(self):
        return self.trademark_name

    def get_absolute_url(self):
        return reverse('stores:shop_detail', kwargs={'pk': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название')
    slug = models.SlugField(max_length=200, db_index=True)
    shops = models.ManyToManyField(Shop, verbose_name='Магазины', related_name='categories', blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Список категорий"
        ordering = ('-name', )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stores:category_detail', kwargs={'pk': self.pk})


class Product(models.Model):
    name = models.CharField(max_length=80, verbose_name='Название')
    category = models.ForeignKey(Category, verbose_name='Категория', related_name='products', blank=True,
                                 on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = "Список продуктов"
        ordering = ('-name',)

    def __str__(self):
        return self.name


class ProductInfo(models.Model):
    model = models.CharField(max_length=80, verbose_name='Модель', blank=True)
    external_id = models.PositiveIntegerField(verbose_name='Внешний ID')
    product = models.ForeignKey(Product, verbose_name='Продукт', related_name='product_infos', blank=True,
                                on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, verbose_name='Магазин', related_name='product_infos', blank=True,
                             on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    price = models.PositiveIntegerField(verbose_name='Цена')
    price_rrc = models.PositiveIntegerField(verbose_name='Рекомендуемая розничная цена')

    class Meta:
        verbose_name = 'Информация о продукте'
        verbose_name_plural = "Информационный список о продуктах"
        constraints = [
            models.UniqueConstraint(fields=['product', 'shop', 'external_id'], name='unique_product_info'),
        ]


class Parameter(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название')

    class Meta:
        verbose_name = 'Имя параметра'
        verbose_name_plural = "Список имен параметров"
        ordering = ('-name',)

    def __str__(self):
        return self.name


class ProductParameter(models.Model):
    product_info = models.ForeignKey(ProductInfo, verbose_name='Информация о продукте',
                                     related_name='product_parameters', blank=True,
                                     on_delete=models.CASCADE)
    parameter = models.ForeignKey(Parameter, verbose_name='Параметр', related_name='product_parameters', blank=True,
                                  on_delete=models.CASCADE)
    value = models.CharField(verbose_name='Значение', max_length=100)

    class Meta:
        verbose_name = 'Параметр'
        verbose_name_plural = "Список параметров"
        constraints = [
            models.UniqueConstraint(fields=['product_info', 'parameter'], name='unique_product_parameter'),
        ]