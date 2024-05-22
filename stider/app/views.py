from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Signup
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt 
import razorpay
from django.db.models import Q

# Create your views here.

def home(req):
    return render(req,'index.html')
def signup(req):
    if(req.method=='GET'):
        return render(req,'signup.html')
    else:
        name=req.POST.get('name')
        email=req.POST.get('email')
        phone=req.POST.get('phone')
        password=req.POST.get('password')
        obj=Signup(name=name,email=email,phone=phone,password=password)
        obj.save()
        return redirect('/login')
def login(req):
    if(req.method=='get'):
        return render(req,'login.html')
    else:
        email=req.POST.get('email')
        password=req.POST.get('password')
        if Signup.login_user(email,password):
            data=Signup.objects.all()
            return render(req,'base.html',{'key':data})
        else:
            msg="Incorrect User Id and Password"
            return render(req,'login.html',{'error':msg})
def base(req):
    return render(req,'base.html')
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

def order_confirm(request):
    return redirect('/payment')
def payment(request):
    total=request.POST.get('total')
    #amt=request.POST.get("total")
    currency = 'INR'

    #amount = amt*100
    amt=int(total)
    #amt = request.POST.get("total")
    amount = amt * 100


    print(amt)
    razorpay_order = razorpay_client.order.create(dict(
            amount=amount,
            currency=currency,
            payment_capture='0'))

    razorpay_order_id = razorpay_order['id']
    callback_url = '/orderPlaced'

    context = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_merchant_key': settings.RAZOR_KEY_ID,
            'razorpay_amount': amount,
            'currency': currency,
            'callback_url': callback_url,
        }
    

    return render(request, 'order_confirm.html', context=context)
@csrf_exempt
def orderPlaced(req):
    #cart_view=Cart.objects.all()
    return HttpResponse('Thank you')
def showdata(req):
    data=Signup.objects.all()
    return render(req,'showdata.html',{'key':data})
def search(request):
    query = request.GET.get('email')
    data = []
    if query:
        data = Signup.objects.filter(Q(email__icontains=query)| Q(phone=query))
    return render(request, 'showdata.html', {'key': data})
def logout(req):
    return redirect('/')

def delet(req):
    
    signup_instance = Signup.objects.get(pk=roll)
    signup_instance.delete()
    return redirect("showdata.html")


        