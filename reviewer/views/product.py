from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from reviewer.forms import ProductForm
from reviewer.models import Product


class ModeratorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='Moderators').exists()


class ProductListView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 8


class ProductCreateView(ModeratorRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('index')


class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        reviews_list = product.reviews.all()
        paginator = Paginator(reviews_list, 3)

        page = self.request.GET.get('page')
        reviews = paginator.get_page(page)

        context['reviews'] = reviews
        return context


class ProductUpdateView(ModeratorRequiredMixin, UpdateView):
    model = Product
    fields = ['name', 'category', 'description', 'image']
    template_name = 'product_update.html'
    success_url = reverse_lazy('index')


class ProductDeleteView(ModeratorRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('inde')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(pk=self.kwargs['pk'])
