from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('signup',views.signup),
    path('login',views.login),
    path('order_confirm',views.order_confirm),
    path('payment',views.payment),
    path('base',views.base),
    path('orderPlaced',views.orderPlaced),
    path('showdata',views.showdata),
    path('search',views.search),
    path('delet/<int:roll>/', views.delet, name='delet'),
]


