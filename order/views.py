from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView
from order.models import Order
from catalog.models import Product

class OrderCreateView(CreateView):
    model = Order
    fields = ('product', 'name', 'email', 'message',)


    def get_success_url(self):
        return reverse('catalog:product', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['product'] = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        return context_data
