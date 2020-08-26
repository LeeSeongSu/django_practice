from django.urls import path

from . import views
import shop.views
app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/order/new/', views.order_new, name='order_new'),
    path('<int:item_id>/order/<str:merchant_uid>/pay/', views.order_pay, name='order_pay'),
    path('meet_create', shop.views.meet_create, name='meet_create'),
]
