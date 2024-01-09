from django.shortcuts import render, redirect
from Newapp.models import CategoryDb, ProductDb
from Frontend.models import ContactDb, UserRegDb, CartDB, OrderDb
from django.contrib import messages


def homepage(request):
    cat = CategoryDb.objects.all()
    return render(request, "Home.html", {'cat': cat})


def pro_view(request):
    pro = ProductDb.objects.all()
    return render(request, "productpage.html", {'pro': pro})


def show_pro_each(request, cat_id):
    data = ProductDb.objects.filter(Cat_name=cat_id)
    return render(request, "show_pro.html", {'data': data})


def sing_product(request, code_id):
    data = ProductDb.objects.get(id=code_id)
    return render(request, "Singleproduct.html", {'data': data})


def about_us(request):
    return render(request, "about_us.html")


def services(request):
    return render(request, "service.html")


def contact(request):
    return render(request, "contact_us.html")


def save_contact(request):
    if request.method == "POST":
        fna = request.POST.get('first-name')
        lna = request.POST.get('last-name')
        ema = request.POST.get('email')
        adr = request.POST.get('address')
        cit = request.POST.get('city')
        con = request.POST.get('country')
        tel = request.POST.get('tel')
        mes = request.POST.get('message')
        obj = ContactDb(Firstname=fna, Lastname=lna, Email=ema, Address=adr, City=cit, Country=con, Telephone=tel, Message=mes)
        obj.save()
        messages.success(request, "Contact Added Successfully!!...")
        return redirect(contact)


def user_log_page(request):
    return render(request, "Register.html")


def sign_up_page(request):
    return render(request, "Signup.html")


def save_sign_det(request):
    if request.method == "POST":
        nam = request.POST.get('name')
        us = request.POST.get('username')
        ema = request.POST.get('email')
        pas = request.POST.get('password')
        num = request.POST.get('number')
        obj = UserRegDb(name=nam, username=us, email=ema, pass_word=pas, Mob_number=num)
        obj.save()
        messages.success(request, "Account Created Successfully!!...")
        return redirect(user_log_page)


def userlogin(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        if UserRegDb.objects.filter(username=un, pass_word=pwd).exists():
            request.session['username'] = un
            request.session['pass_word'] = pwd
            messages.success(request, "Logged in Successfully!!...")
            return redirect(homepage)
        else:
            messages.error(request, "Username or password is Incorrect!!...")
            return redirect(user_log_page)
    else:
        return redirect(user_log_page)


def userlogout(request):
    del request.session['username']
    del request.session['pass_word']
    messages.success(request, "logged out Successfully!!...")
    return redirect(user_log_page)


def cart_page(request):
    info = CartDB.objects.filter(Username=request.session['username'])
    total_price = 0
    for j in info:
        total_price = total_price + j.Total_price
    return render(request, "Cart.html", {'info': info, 'total_price':total_price})


def save_cart(request):
    if request.method == "POST":
        usname = request.POST.get('uname')
        pname = request.POST.get('pdtname')
        quan = request.POST.get('quant')
        tprice = request.POST.get('tprc')
        des = request.POST.get('description')
        obj = CartDB( Username =usname, Prod_name=pname, Quantity=quan, Total_price=tprice, Description=des)
        obj.save()
        messages.success(request, "Cart Added Successfully!!...")
        return redirect(cart_page)


def rem_cart(request,dataid):
    rem = CartDB.objects.filter(id=dataid)
    rem.delete()
    messages.error(request, "Cart removed Successfully!!...")
    return redirect(cart_page)


def checkout_page(request):
    data = CartDB.objects.filter(Username=request.session['username'])
    total_price = 0
    for i in data:
        total_price = total_price + i.Total_price
    return render(request, "Checkout.html", {'data': data, 'total_price': total_price})


def save_check(request):
    if request.method == "POST":
        fname = request.POST.get('first-name')
        lname = request.POST.get('last-name')
        mail = request.POST.get('email')
        ad = request.POST.get('address')
        cit = request.POST.get('city')
        con = request.POST.get('country')
        zi = request.POST.get('zip-code')
        tl = request.POST.get('tel')
        obj = OrderDb(First_name=fname, Last_name=lname, E_mail=mail, A_dress=ad, C_ity=cit, Country=con, Zipcode=zi, Tele=tl)
        obj.save()
        messages.success(request, "Order Placed Successfully!!...")
        return redirect(homepage)







