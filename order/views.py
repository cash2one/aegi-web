from django.shortcuts import render
from order.forms import orderForm
from django.shortcuts import HttpResponseRedirect

# Create your views here.
def order(request):
    return render(request, 'order/order.html')

def pay(request):
    if request.method == 'POST':
        if 'type' in request.POST:
            postType = request.POST['type']
            if postType == 'file':
                myForm = orderForm(request.POST)

                if myForm.is_valid():
                    myForm.save()
                    return HttpResponseRedirect('/order/payment')


    myForm = orderForm()
    return render(request, 'order/pay.html',locals())