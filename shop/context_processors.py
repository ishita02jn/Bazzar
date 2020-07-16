from .models import Order, Order_item, Coupon_Dis

def cart_total(request):
    quantity = 0
    sub_total = 0
    discount = 0
    total = 0
    if request.user.is_authenticated:
        obj= Order.objects.filter(user_id = request.user, completed = False)
        if obj:
            items = Order_item.objects.filter(order_id = obj[0])
            for item in items:
                quantity+=item.quantity
                sub_total+= (item.prod_id.price * item.quantity)
            discount_coup = obj[0].coupon
            if discount_coup is not None:
                coupon = Coupon_Dis.objects.get(coupon_id=discount_coup.coupon_id)
                discount_per = coupon.discount_percent
                discount = (sub_total*discount_per)//100
            total = sub_total-discount 

    return{
        'cart_total': quantity,
        'sub_total': sub_total,
        'discount': discount,
        'total': total
    }
