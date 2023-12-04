from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contact, ProductListView, ProductDetailView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name='index'),
    path("contact/", contact, name='contact'),
    path("product/<int:pk>/", ProductDetailView.as_view(), name='product'),
    path("category_list/", CategoryListView.as_view(), name='category_list'),
]
