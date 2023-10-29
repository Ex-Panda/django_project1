from django.urls import path

from catalog.views import ProductsListView, ProductDetailView, ContactsTemplateView

app_name = 'catalog'

urlpatterns = [
    path('', ProductsListView.as_view(), name='home'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
]
