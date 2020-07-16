from django.urls import path
from . import views

urlpatterns = [
    # ----- Login/Signup ------
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('signup/', views.register, name="signup"),

    # ----- Basic ------
    path('', views.home, name="home"),
    path('s/', views.search, name="search"),
    path('product/<int:prod_id>/', views.single_product, name="product"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('myorders/', views.my_orders, name="myorders"),

    # ----- Checkout ------
    path('payment/', views.payment, name='shop_payment'),
    path('handlepayment/', views.handlepayment, name='shop_handlepayment'),
    path('deliver/', views.shipping_address, name = 'deliver'),
    path('checkout/', views.checkout, name="checkout"),

    # ----- Cart ------
    path('cart/', views.cart, name="cart"),
    path('addtocart/<int:prod_id>/', views.add_to_cart, name="add_to_cart"),
    path('removefromcart/<int:prod_id>/', views.remove_from_cart, name="remove_from_cart"),
    path('updatequantity+/<int:orderitem_id>/', views.update_quantity_plus, name="update_quantity_plus"),
    path('updatequantity-/<int:orderitem_id>/', views.update_quantity_minus, name="update_quantity_minus"),
    path('applycoupon/', views.apply_coupon, name='shop_applycoupon')
    
]