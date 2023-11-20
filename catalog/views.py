from django.core.cache import cache
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Version
from config import settings


class ProtectedView(View):
    #переопределение get, чтобы анонимный пользователь не мог взаимодействовать с продуктами
    def get(self, *args, **kwargs):
        if self.request.user.id is None:
            return redirect('user_auth:login')
        else:
            return super().get(*args, **kwargs)


class ProductsListView(ListView):
    model = Product
    template_name = 'catalog/home.html'


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
        return render(request, self.template_name)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["versions"] = Version.objects.filter(product=self.kwargs['pk'])
        return context


class ProductCreateView(ProtectedView, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.user = self.request.user
            new_product.save()

        return super().form_valid(form)


class ProductUpdateView(ProtectedView, UpdateView):
    model = Product
    form_class = ProductForm

    def get_object(self, queryset=None):
        #переопределяю метод, получаю объект, проверяю пользователя по требованиям
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user and not self.request.user.is_superuser and not self.request.user.has_perm('catalog.product_published'):
            raise Http404
        return self.object

    def get_success_url(self):
        return reverse('catalog:product', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        if self.request.user.has_perm('catalog.product_published'):
            return ProductModeratorForm
        else:
            return ProductForm


class VersionCreateView(ProtectedView, CreateView):
    model = Version
    form_class = VersionForm

    def get_success_url(self):
        return reverse('catalog:product', args=[self.kwargs.get('pk')])

    def form_valid(self, form):
        form.instance.product_id = self.kwargs['pk']
        return super().form_valid(form)
