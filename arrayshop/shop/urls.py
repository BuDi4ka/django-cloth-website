from django.urls import path
from . import views


app_name = "shop"


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('category/<slug:slug>/', views.product_list, name='product_list_by_slug'),
    path('<int:product_id>/<slug:slug>', views.product_detail, name='product_detail'),
]