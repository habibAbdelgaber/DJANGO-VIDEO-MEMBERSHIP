from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.views.generic import DetailView, UpdateView
from django.urls import reverse
from django.views.generic import FormView
import stripe

from .forms import CancelSubscriptionForm

User = get_user_model()

stripe.api_key = settings.STRIPE_SECRET_KEY

class CancelSubscriptionView(LoginRequiredMixin, FormView, DetailView):
    form_class = CancelSubscriptionForm

    def get_success_url(self):
        return reverse('users:detail', kwargs={'username': self.request.user.username})

    def form_valid(self, form):
        stripe.Subscription.delete(self.request.user.subscription.stripe_subscription_id)
        messages.success(self.request, 'You have successfully cancelled your subscription!')
        return super().form_valid(form)

class UserSubscriptionView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = 'users/user_subscription.html'



class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/user_detail.html'

    slug_field = "username"
    slug_url_kwarg = "username"

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ["username"]

    template_name = 'users/user_form.html'

    def get_success_url(self):
        return reverse('users:detail', kwargs={'username': self.request.user.username})

    def get_object(self):
        return User.objects.get(username=self.request.user.username)

    def form_invalid(self, form):
        return super().form_valid(form)
