from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=100, verbose_name="slug", **NULLABLE)
    content = models.TextField(verbose_name='содержимое', **NULLABLE)
    preview = models.ImageField(upload_to='product/', verbose_name='изображение', **NULLABLE)
    date_create = models.DateTimeField(verbose_name='дата создания', **NULLABLE)
    is_published = models.BooleanField(default=True, verbose_name='признак публикации')
    count_views = models.IntegerField(default=0, verbose_name='количество просмотров')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
