from django.db import models

class Order(models.Model):
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE, verbose_name='продукт')

    name = models.CharField(max_length=150, verbose_name='имя')
    email = models.EmailField(max_length=150, verbose_name='почта')
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False, verbose_name='заказ закрыт')


    def __str__(self):
        return f'{self.product} от {self.email}'


    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
