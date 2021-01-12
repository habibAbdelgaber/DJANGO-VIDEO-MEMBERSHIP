from django.urls import path
from .views import UserDetailView, UserUpdateView, UserSubscriptionView, CancelSubscriptionView


app_name = 'users'

urlpatterns = [
    path('update/', UserUpdateView.as_view(), name='update'),
    path('<str:username>/', UserDetailView.as_view(), name='detail'),
    path("<str:username>/subscription/", UserSubscriptionView.as_view(), name='subscription'),
    path("<str:username>/subscription/cancel/", CancelSubscriptionView.as_view(), name='cancel-subscription')
]