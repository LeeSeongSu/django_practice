from django.conf.urls import url
from . import views
from django.urls import path
import shop.views

app_name='shop'
urlpatterns = [
    
    url(r'^$', views.ItemListView.as_view(), name='index'),
    url(r'^(?P<item_id>\d+)/order/new/$', views.order_new, name='order_new'),
    path('meet_create', shop.views.meet_create, name='meet_create'),
]