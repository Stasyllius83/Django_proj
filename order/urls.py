from django.urls import path
from order.views import OrderCreateView
from order.apps import OrderConfig
from django.views.decorators.cache import never_cache

app_name = OrderConfig.name

urlpatterns = [
    path("create/<int:pk>", never_cache(OrderCreateView.as_view()), name='create'),
]
