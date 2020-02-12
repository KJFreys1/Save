from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_list, name='list_list'),
    path('lists/<int:pk>', views.list_detail, name='list_detail'),
    path('lists/new', views.list_create, name='list_create'),
    path('lists/<int:pk>/update', views.list_update, name='list_update'),
    path('lists/<int:pk>/delete', views.list_delete, name='list_delete'),
    path('items/<int:pk>/update', views.item_update, name='item_update'),
    path('items/<int:pk>/grey', views.item_grey, name='item_grey'),
    path('items/<int:pk>/delete', views.item_delete, name='item_delete'),
]