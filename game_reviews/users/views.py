from decimal import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.db.models import Sum
from django.conf import settings
import stripe

from .models import UserProfile


def user_profile_view(request):

    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Creates Stripe payment intent
    payment_intent = stripe.PaymentIntent.create(
        amount='295',
        currency='usd',
        payment_method_types=['card']
    )

    # payment_intent.client_secret used on client side for javascript to render the card
    context = {
        'secret_key': payment_intent.client_secret,
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
        'payment_intent_id': payment_intent.id,
    }

    return render(request, "user_profile.html", context)


def pay_thankyou_view(request):

    payment_intent_secret = request.POST['payment_intent_secret']
    payment_intent_id = request.POST['payment_intent_id']
    payment_method_id = request.POST['payment_method_id']
    stripe_plan_id = settings.STRIPE_PLAN_ANNUALY_PRICE_ID
    auto_renew = request.POST['auto-renew-check']
    stripe.api_key = settings.STRIPE_SECRET_KEY 
    
    print("payment_intent_secret: " + payment_intent_secret)
    print("payment_intent_id: " + payment_intent_id)
    print("payment_method_id: " + payment_method_id) 
    print("stripe_plan_id: " + stripe_plan_id) 
    print("stripe.api_key: " + stripe.api_key) 
    print("auto_renew: " + auto_renew) 

    #region Non 3d-Secure
    if auto_renew == 'on':
        customer = stripe.Customer.create(
            email=request.POST['user_email'],
            payment_method=payment_method_id,
            invoice_settings={
                'default_payment_method': payment_method_id
            }
        )
        stripe.Subscription.create(
            customer=customer.id,
            items=[
                {
                    'plan': stripe_plan_id
                },
            ]
        )
        stripe.PaymentIntent.modify(
            payment_intent_id,
            payment_method = payment_method_id,
            customer=customer.id
        )
    else:    
        stripe.PaymentIntent.modify(
            payment_intent_id,
            payment_method = payment_method_id
        )  
        stripe.PaymentIntent.confirm(
            payment_intent_id
        )
    #endregion

    ret = stripe.PaymentIntent.confirm(payment_intent_id)

    if ret.status == 'requires_action':
        pi = stripe.PaymentIntent.retrieve(payment_intent_id)
        
        context = {
            '3dsec': True,
            'payment_intent_secret': pi.client_secret,
        }
        return render(request, "pay_thankyou.html", context)
    else:
        context = {}
        return render(request, "pay_thankyou.html", context)
    