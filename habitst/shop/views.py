from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import Item, Order
from .forms import PayForm,ItemForm
from appname.forms import HashtagForm

class ItemListView(ListView):
    model = Item
    queryset = Item.objects.filter(is_public=True)

    def get_queryset(self):
        self.q = self.request.GET.get('q', '')
        qs = super().get_queryset()

        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs

    def get_context_data(self, **kwargs):
        context = super(ItemListView,self).get_context_data(**kwargs)
        context['q'] = self.q
        context['Order_list'] = Order.objects.all()
      
        return context


index = ItemListView.as_view()
# Create your views here.


@login_required
def order_new(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    order = Order.objects.create(user=request.user, item=item, name=item.name, amount=item.amount)
    return redirect('shop:order_pay', item_id, str(order.merchant_uid))


@login_required
def order_pay(request, item_id, merchant_uid):
    order = get_object_or_404(Order, user=request.user, merchant_uid=merchant_uid, status='ready')
    if request.method == 'POST':
        form = PayForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('mypage')
    else:
        form = PayForm(instance=order)
    return render(request, 'shop/pay_form.html', {
        'form': form,
    })

def meet_create(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.meet_writer = request.user           
            post.save()
            return redirect('./')
    else:
        form = ItemForm()
        return render(request, 'shop/meet_create.html', {'form': form})


