from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages 
from django.conf import settings
from .forms import OrderForm
import stripe
from products.models import Product
from .models import OrderLineItem, Order
from cart.contexts import cart_contents

# Create your views here.
def checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        cart = request.session.get('cart', {})   

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
        } 

        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(order=order, product=product, quantity=item_data)
                    order_line_item.save()

                except Product.DoesNotExist:
                    messages.error(request, ("One of the products in your bag was not found in the database." 
                    " Please contact us for further assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            request.session['save_info'] = 'save_info' in request.POST        
            return redirect(reverse('checkout_success', args=[order.order_number]))    
        else:
            messages.error(request, 'There was a problem with your order form. Please double check your details')    

    else:    
        #Redirect user back to the shop if their cart is empty
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, 'Your Cart is empty!')
            return redirect(reverse('products'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']   
        stripe_total = round(total * 100) 
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total, 
            currency = settings.STRIPE_CURRENCY,
        )

        print(intent)


        order_form = OrderForm()
    
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,

    }

    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):

    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully placed! \
        Your order number is {order_number}. A confirmation email \
            will be send to {order.email} ')

    if 'cart' in request.session:
        del request.session['cart']

    context  = {
        'order': order,
    }  

    return render(request, 'checkout/checkout_success.html', context)   