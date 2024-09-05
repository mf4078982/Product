from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('product_create/',views.product_create,name='product_create'),
    path('list_product/',views.product_list,name='product_list'),
    path('update/<int:product_id>/',views.update_view,name='update_view'),
    path('delete/<int:product_id>/',views.product_delete,name='product_delete'),
]
