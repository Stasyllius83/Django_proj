from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contact, index, product, category_index

app_name = CatalogConfig.name

urlpatterns = [
    path("", index, name='index'),
    path("contact/", contact, name='contact'),
    path("product/<int:pk>/", product, name='product'),
    path("category_list/", category_index, name='category_list'),
]
