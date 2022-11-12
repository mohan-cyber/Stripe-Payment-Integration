from django.urls import path
from . import views


urlpatterns = [
    path('test-payment/', views.StripeView.as_view(),name='checkout-stripe'),
    path('save-stripe-info/', views.StripeView.as_view(),name='save-stripe-info'),

]