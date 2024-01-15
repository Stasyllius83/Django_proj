from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=250, verbose_name='описание')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):

    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=250, verbose_name='описание')
    picture = models.ImageField(upload_to='product/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена')
    date = models.DateField(verbose_name='дата создания')
    last_date_change = models.DateField(verbose_name='дата последнего изменения')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='продавец')

    is_published = models.BooleanField(default=False, verbose_name='признак публикации')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        permissions = [
            ('set_is_published', 'Может менять статус публикации'),
            ('set_description', 'Может изменять описание'),
            ('set_category', 'Может изменять категорию'),
        ]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    num_version = models.IntegerField(verbose_name='номер версии')
    name_version = models.CharField(max_length=100, verbose_name='название версии')
    status_version = models.BooleanField(default=False, verbose_name='активная версия')

    def __str__(self):
        return f'{self.product}({self.num_version}) - {self.name_version}'


    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
