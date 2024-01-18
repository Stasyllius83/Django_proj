from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView
from django.views.decorators.cache import cache_page, never_cache

app_name = BlogConfig.name

urlpatterns = [
    path("create/", never_cache(BlogCreateView.as_view()), name='create'),
    path("", BlogListView.as_view(), name='list'),
    path("view/<int:pk>/", cache_page(60)(BlogDetailView.as_view()), name='view'),
    path("edit/<int:pk>/", never_cache(BlogUpdateView.as_view()), name='edit'),
    path("delete/<int:pk>/", BlogDeleteView.as_view(), name='delete'),
]
