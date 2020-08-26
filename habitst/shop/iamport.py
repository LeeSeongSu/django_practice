from django.contrib import admin
from .models import Item, Order
from django.utils.html import mark_safe
from iamport import Iamport

def do_cancel(self, request, queryset):
        '결제내역 취소'
        queryset = queryset.filter(status='paid')
        total = queryset.count()

        if total > 0:
            for order in queryset:
                order.cancel()
            self.message_user(request, '주문 {}건을 취소했습니다.'.format(total))
        else:
            self.message_user(request, '취소할 주문이 없습니다.')

    do_cancel.short_description = '선택된 주문에 대해 결제취소요청하기'
