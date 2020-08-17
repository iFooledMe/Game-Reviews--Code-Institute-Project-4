from decimal import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.db.models import Sum
from django.conf import settings
import stripe


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
        'payment_intent_id': payment_intent.id
    }

    return render(request, "user_profile.html", context)


def pay_thankyou_view(request):
    request.POST['payment_intent_id']
    request.POST['payment_method_id']
    
    context = {}
    return render(request, "pay_thankyou.html", context)
