from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    url(r'^$', views.index, name='index', kwargs={'template_name': 'shop/item_list.html'}),
    url(r'^(?P<item_id>\d+)/order/new/$', views.order_new, name='order_new'),
    url(r'^(?P<item_id>\d+)/order/(?P<merchant_uid>[\da-f\-]{36})/pay/$', views.order_pay, name='order_pay'),
    path('meet_create', views.meet_create, name='meet_create'),
    
]
