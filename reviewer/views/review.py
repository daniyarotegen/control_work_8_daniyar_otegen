from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from reviewer.models import Review, Product
from reviewer.forms import ReviewForm


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.product = Product.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_initial(self):
        initial_data = super().get_initial()
        initial_data['author'] = self.request.user
        initial_data['product'] = Product.objects.get(pk=self.kwargs['pk'])
        return initial_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.get(pk=self.kwargs['pk'])
        return context

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.kwargs['pk']})


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review_update.html'

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.object.product.pk})

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.author or self.request.user.groups.filter(name='Moderators').exists()


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = 'review_delete.html'

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.object.product.pk})

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.author or self.request.user.groups.filter(name='Moderators').exists()

