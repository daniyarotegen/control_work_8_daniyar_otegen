from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import UpdateView, CreateView, RedirectView
from accounts.forms import CustomUserChangeForm, CustomUserCreationForm
from reviewer.models import Review


class UserProfileView(LoginRequiredMixin, View):
    template_name = 'user_profile.html'

    def get(self, request, user_id):
        User = get_user_model()
        user = User.objects.get(pk=user_id)
        reviews = Review.objects.filter(author=user)
        return render(request, self.template_name, {'user': user, 'reviews': reviews})


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'user_update.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        user_id = self.object.pk
        return reverse('user_profile', kwargs={'user_id': user_id})


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class CurrentUserProfileView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        user_id = self.request.user.id
        return reverse('user_profile', args=[user_id])
