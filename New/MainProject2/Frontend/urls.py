from django.urls import path
from Frontend import views


urlpatterns = [
    path('homepage/', views.homepage, name="homepage"),
    path('pro_view/', views.pro_view, name="pro_view"),
    path('show_pro_each/<cat_id>/', views.show_pro_each, name="show_pro_each"),
    path('sing_product/<int:code_id>/', views.sing_product, name="sing_product"),
    path('about_us/', views.about_us, name="about_us"),
    path('services/', views.services, name="services"),
    path('contact/', views.contact, name="contact"),
    path('save_contact/', views.save_contact, name="save_contact"),
    path('user_log_page/', views.user_log_page, name="user_log_page"),
    path('sign_up_page/', views.sign_up_page, name="sign_up_page"),
    path('save_sign_det/', views.save_sign_det, name="save_sign_det"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('cart_page/', views.cart_page, name="cart_page"),
    path('save_cart/', views.save_cart, name="save_cart"),
    path('rem_cart/<int:dataid>/', views.rem_cart, name="rem_cart"),
    path('checkout_page/', views.checkout_page, name="checkout_page"),
    path('save_check/', views.save_check, name="save_check"),




]