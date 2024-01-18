from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import CategoryProduct, ProductDeleteView, contact, ProductListView, ProductDetailView,\
      CategoryListView, ProductCreateView, ProductUpdateView
from django.views.decorators.cache import cache_page, never_cache

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name='index'),
    path("contact/", contact, name='contact'),
    path("product/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name='product'),
    path("category_list/", CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryProduct.as_view(), name='category_products'),
    path("create/", never_cache(ProductCreateView.as_view()), name='create_product'),
    path("update/<int:pk>", never_cache(ProductUpdateView.as_view()), name='update_product'),
    path("delete/<int:pk>", ProductDeleteView.as_view(), name='delete_product'),
]
