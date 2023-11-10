from django.urls import path

from catalog.views import ProductsListView, ProductDetailView, ContactsTemplateView, ProductCreateView, \
    ProductUpdateView, VersionCreateView

app_name = 'catalog'

urlpatterns = [
    path('', ProductsListView.as_view(), name='home'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('create_version/<int:pk>', VersionCreateView.as_view(), name='create_version'),
]
