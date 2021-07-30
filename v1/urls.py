"""v1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from views import views, orders, users

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('home/', views.home, name="home"),
    url('login/', views.login, name="login"),
    url('orders/<orderid>', orders.order, name="order_id"),
    url('orders/<order_ids>', orders.orders, name="orders_ids"),
    url('orders/dates', orders.dates, name="dates"),
    url('orders/shipping/<key>', orders.shipping, name="shipping"),
    url('orders/<user_id>', users.user_orders, name="user_orders"),
    url('users/all', users.all_users, name="users"),
    url('users/<user_id>', users.user_id, name="user_id"),
    url('orders/search', orders.search, name="search"),
]
