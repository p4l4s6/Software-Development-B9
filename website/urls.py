from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('subscribe/', views.SubscriberView.as_view(), name='subscribe'),
]
