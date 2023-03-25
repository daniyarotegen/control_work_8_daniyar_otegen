from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from reviewer.forms import ProductForm
from reviewer.models import Product


class IndexView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 8


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('index')


class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'category', 'description', 'image']
    template_name = 'product_update.html'
    success_url = reverse_lazy('index')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('inde')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(pk=self.kwargs['pk'])



