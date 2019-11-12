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
    official_name = models.CharField(max_length=50, verbose_name='Наименование организации')
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
                                                                  'Загрузите файл с расширением .csv'})

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = "Список магазинов"
        ordering = ('-trademark_name',)

    def __str__(self):
        return f'{self.trademark_name}'
