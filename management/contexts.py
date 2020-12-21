from django.conf import settings
from django.shortcuts import get_object_or_404
from .models import Sitesettings



""" This context file will allow all pages to access the site settings """

def setting_contents(request):

    #Free Shipping
    free_shipping = get_object_or_404(Sitesettings, name="Free Shipping Threshold")
    free_shipping_setting = free_shipping.status
    free_shipping_threshold = free_shipping.value
  
    context = {
        'free_shipping_setting': free_shipping_setting,
        'free_shipping_threshold': free_shipping_threshold
    }


    return context