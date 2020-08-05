from django.shortcuts import render
from .models import Order
from django.views.generic import UpdateView, TemplateView, ListView, DetailView, DeleteView
from cart.models import Cart
from django.urls import reverse_lazy

class OrderDetailView(DetailView):
    model = Order
    template_name = 'order/detail.html'

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order/delete.html'
    success_url = reverse_lazy('order:done2')

class OrderListView(ListView):
    model = Order
    template_name = 'order/list.html'
    paginate_by = 10

class OrderDone(TemplateView):
    template_name = 'order/done.html'

class OrderDone2(TemplateView):
    template_name = 'order/done2.html'

class CreateOrder(UpdateView):
    model = Order
    template_name = 'order/create.html'
    fields = (
        'delivery_address','contact_phone',
    )

    def get_object(self):
        cart_id = self.request.session.get('cart_pk')
        if cart_id:
            cart = Cart.objects.get(pk = cart_id)
            try:
                order_pk = cart.order.pk
            except:
                order_pk = None

        obj, created = self.model.objects.get_or_create(
            pk = order_pk,
            defaults = {
                'cart':cart,
                'status':False,
                'delivery_address':'Введите пожалуйста адрес доставки',
                'contact_phone':'Введите пожалуйста контактный номер мобильного телефона (Вида +375291234567)',
            }
        )
        return obj

    def get_success_url(self):
        url = reverse_lazy('order:done')
        self.object.status = True
        self.object.save()
        del(self.request.session['cart_pk'])
        return url