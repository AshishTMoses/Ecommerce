from django.shortcuts import render, redirect
from Newapp.models import CategoryDb, ProductDb
from Frontend.models import ContactDb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# Create your views here.


def intro_page(request):
    return render(request, "index.html")


def add_product_page(request):
    return render(request, "AddProduct.html")


def save_category(request):
    if request.method == "POST":
        na = request.POST.get('name')
        des = request.POST.get('description')
        img = request.FILES['image']
        obj = CategoryDb(Name=na, Description=des, Image=img)
        obj.save()
        return redirect(add_product_page)


def disp_category(request):
    disp = CategoryDb.objects.all()
    return render(request, "disp_cat_pr.html", {'disp': disp})


def edit_category(request, dataid):
    edit = CategoryDb.objects.get(id=dataid)
    return render(request, "edit_cat_pr.html", {'edit': edit})


def update_category(request, dataid):
    if request.method == "POST":
        cna = request.POST.get('name')
        desc = request.POST.get('description')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = CategoryDb.objects.get(id=dataid).Image
        CategoryDb.objects.filter(id=dataid).update(Name=cna, Description=desc, Image=file)
        return redirect(disp_category)


def remv_category(request, dataid):
    rem = CategoryDb.objects.filter(id=dataid)
    rem.delete()
    return redirect(disp_category)


def add_product_cat(request):
    category = CategoryDb.objects.all()
    return render(request, "Add_Prod_cat.html", {'category': category})


def save_product(request):
    if request.method == "POST":
        cna = request.POST.get('cat')
        pna = request.POST.get('pname')
        descr = request.POST.get('pdescription')
        prize = request.POST.get('prize')
        pimg = request.FILES['pimage']
        obj = ProductDb(Cat_name=cna, Pro_name=pna, Description=descr, Price=prize, Pro_image=pimg)
        obj.save()
        return redirect(add_product_cat)


def display_product(request):
    show = ProductDb.objects.all()
    return render(request, "displayProduct.html", {'show': show})


def edit_product(request, pro_id):
    cat = CategoryDb.objects.all()
    product = ProductDb.objects.get(id=pro_id)
    return render(request, "EditProduct.html", {'cat': cat, 'product': product})


def update_product(request, dataid):
    if request.method == "POST":
        cna = request.POST.get('cat')
        pra = request.POST.get('pname')
        descr = request.POST.get('pdescription')
        prize = request.POST.get('prize')

        try:
            img = request.FILES['pimage']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = ProductDb.objects.get(id=dataid).Pro_image
        ProductDb.objects.filter(id=dataid).update(Cat_name=cna, Pro_name=pra, Description=descr, Price=prize, Pro_image=file)
        return redirect(display_product)


def remv_product(request, dataid):
    re = ProductDb.objects.filter(id=dataid)
    re.delete()
    return redirect(display_product)


def admin_login(request):
    return render(request, "AdminLogin.html")


def adminlogin(request):
    if request.method == "POST":
        una = request.POST.get('user_name')
        pwd = request.POST.get('pass_word')

        if User.objects.filter(username__contains=una).exists():
            x = authenticate(username=una, password=pwd)
            if x is not None:
                login(request, x)
                request.session['username'] = una
                request.session['password'] = pwd
                return redirect(intro_page)
            else:
                return redirect(admin_login)
        else:
            return redirect(admin_login)


def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login)


def user_details_disp(request):
    use = ContactDb.objects.all()
    return render(request, "UserDetails.html",{'use': use})


def can_details(request, canid):
    ca = ContactDb.objects.filter(id=canid)
    ca.delete()
    return redirect(user_details_disp)



