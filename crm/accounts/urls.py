from django.urls import path
from . import views as account_views

urlpatterns = [
    path('', account_views.home),
    path('products/', account_views.products),
    path('customer/', account_views.customer)

]
