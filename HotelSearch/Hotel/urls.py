from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('hotel_api/<int:pk>',views.hotel_api,name='hotel_api'),
]
