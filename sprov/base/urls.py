from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('', views.homePage, name='home'),
   path('book/', views.bookingconsultingPage, name = 'book'),
   path('service_page/<str:pk>/', views.servicePage, name='service'),

]

