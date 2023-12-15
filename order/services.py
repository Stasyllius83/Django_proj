from catalog.models import Product
from django.core.mail import send_mail
from django.conf import settings
from order.models import Order


def send_order_email(order_item: Order):
    send_mail(
        'Заявка на покупку продукта',
        f'{order_item.name} ({order_item.email}) хочет купить ваш продукт {order_item.product.name} Сообщение от него: {order_item.message}',
        settings.EMAIL_HOST_USER,
        [order_item.email]
    )
