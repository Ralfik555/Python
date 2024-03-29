from django.urls import path
from . import views as account_views

urlpatterns = [
    path('', account_views.home, name="home"),
    path('products/', account_views.products,name="products"),
    path('customer/<str:pk>', account_views.customer,name="customer"),
    path('create_order/<str:pk>', account_views.createOrder,name="create_order"),
    path('update_order/<str:pk>', account_views.updateOrder,name="update_order"),
    path('delete_order/<str:pk>', account_views.deleteOrder,name="delete_order"),
    path('user/',account_views.userPage, name='user-page'),

    path('register/', account_views.registerPage, name="register"),
	path('login/', account_views.loginPage, name="login"), 
    path('logout/', account_views.logoutUser, name="logout"), 

]
