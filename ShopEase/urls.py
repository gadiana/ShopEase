"""
URL configuration for ShopEase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import index, services, about, contact, login, register, logout_view, create_cart, create_manage, update_cart, insert_data, update_meth_cart, delete_item, delete_cart, unset_cart_session, view_cart, delete_selected, edit_list_item, save_list_edit

urlpatterns = [
    path('', index, name='index'),
    path('index', index, name='index'),
    path('services/', services, name='services'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('admin/', admin.site.urls),
    
    path('create_cart/', create_cart, name='create_cart'),
    path('create_manage/<int:cart_id>/', create_manage, name='create_manage'),
    path('update_meth_cart/<int:cart_id>/', update_meth_cart, name='update_meth_cart'),
    path('update_cart/<int:cart_id>/', update_cart, name='update_cart'),
    path('insert_data/<int:cart_id>/', insert_data, name='insert_data'),
    path('delete_item/<int:item_id>/', delete_item, name='delete_item'),
    path('delete_cart/<int:cart_id>/', delete_cart, name='delete_cart'),
    path('view_cart/<int:cart_id>/', view_cart, name='view_cart'),
    path('delete_selected/', delete_selected, name='delete_selected'),
    path('edit-list-item/<int:list_id>/', edit_list_item, name='edit_list_item'),
    path('save_list_edit/<int:list_id>/', save_list_edit, name='save_list_edit'),
    path('unset_cart_session/', unset_cart_session, name='unset_cart_session'),
]
