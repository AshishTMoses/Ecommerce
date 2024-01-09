from django.urls import path
from Newapp import views

urlpatterns = [
    path('intro_page/', views.intro_page, name="intro_page"),
    path('add_product_page/', views.add_product_page, name="add_product_page"),
    path('save_category/', views.save_category, name="save_category"),
    path('disp_category/', views.disp_category, name="disp_category"),
    path('edit_category/<int:dataid>/', views.edit_category, name="edit_category"),
    path('update_category/<int:dataid>/', views.update_category, name="update_category"),
    path('remv_category/<int:dataid>/', views.remv_category, name="remv_category"),
    path('add_product_cat/', views.add_product_cat, name="add_product_cat"),
    path('save_product/', views.save_product, name="save_product"),
    path('display_product/', views.display_product, name="display_product"),
    path('edit_product/<int:pro_id>/', views.edit_product, name="edit_product"),
    path('update_product/<int:dataid>/', views.update_product, name="update_product"),
    path('remv_product/<int:dataid>/', views.remv_product, name="remv_product"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
    path('user_details_disp/', views.user_details_disp, name="user_details_disp"),
    path('can_details/<int:canid>/', views.can_details, name="can_details"),


]