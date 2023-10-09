from django.urls import path

import catalog
from catalog.views import contacts_page, home

urlpatterns = [
    path('', home),
    path('contacts_page/', contacts_page),
]
