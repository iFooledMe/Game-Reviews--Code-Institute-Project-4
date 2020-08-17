from decimal import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.db.models import Sum
from django.conf import settings
import stripe


def user_profile_view(request, *args, **kwargs):

    stripe.api_key = settings.STRIPE_SECRET_KEY

    payment_intent = stripe.PaymentIntent.create(
        amount='3000',
        currency='usd',
        payment_method_types=['card']
    )

    # payment_intent.client_secret used on client side for javascript to render the card
    context = {
        'secret_key': payment_intent.client_secret,
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
    }

    return render(request, "user_profile.html", context)


'''def payment_method(request):

    stripe.api_key = settings.STRIPE_SECRET_KEY

    payment_intent = stripe.PaymentIntent.create(
        amount=2.95,
        currency='usd',
        payment_method_types=['card']
    )

    # payment_intent.client_secret used on client side for javascript to render the card
    context = {
        'secret_key': payment_intent.client_secret,
        # 'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
        'stripe_publishable_key': 1,
        'some_var': "test"
    }

    if request.method == 'POST':
        print("is_post")
        card_number = request.POST.get('card-number', 'none')
        if card_number != "none":
            print(card_number)
            return render(request, "user_profile.html", context)
        else:
            print("No card number got trough!")
            return render(request, "user_profile.html", context)
    return render(request, "user_profile.html", context)'''
