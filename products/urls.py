from django.contrib import admin
from django.urls import path
import products.views

urlpatterns = [
	path('', products.views.home, name="products_home"),
]