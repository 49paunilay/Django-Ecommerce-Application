from django.contrib import admin
from django.urls import path,include
from .views import index,details,cart_details,contact
urlpatterns = [
    path('',index,name='index'),
    path('<int:id>/',details,name='details'),
    path('cartdetails',cart_details,name='cart_details'),
    path('contact',contact,name='contact')
]
