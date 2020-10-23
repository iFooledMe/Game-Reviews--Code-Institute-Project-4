from decimal import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.db.models import Sum
from django.conf import settings
import stripe
from .forms import EditUserForm
from .models import UserProfile, UserCommentsScore, UserAvatar
from django.contrib.auth.decorators import login_required

# region ==== USER PROFILE ==================================================


@login_required
def user_profile_view(request):
    session_user_comment_scores = UserCommentsScore.objects.filter(
        user__id=request.user.id)
    avatars = UserAvatar.objects.all()

    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Creates Stripe payment intent
    payment_intent = stripe.PaymentIntent.create(
        amount='295',
        currency='usd',
        payment_method_types=['card']
    )

    # payment_intent.client_secret used on client side for javascript to render the card
    context = {
        'comments': session_user_comment_scores,
        'avatars': avatars,
        'secret_key': payment_intent.client_secret,
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
        'payment_intent_id': payment_intent.id,
    }

    return render(request, "user_profile.html", context)
# endregion
# ===========================================================================

# region ==== EDIT USER PROFILE =============================================


@login_required
def user_profile_edit(request):
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('userprofile')
    else:
        # Creates Stripe payment intent
        stripe.api_key = settings.STRIPE_SECRET_KEY

        payment_intent = stripe.PaymentIntent.create(
            amount='295',
            currency='usd',
            payment_method_types=['card']
        )

        session_user_comment_scores = UserCommentsScore.objects.filter(
            user__id=request.user.id)

        user_form = EditUserForm(instance=request.user)
        context = {
            'user_form': user_form,
            'comments': session_user_comment_scores,
            'secret_key': payment_intent.client_secret,
            'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
            'payment_intent_id': payment_intent.id,
        }
        return render(request, "edit_profile.html", context)
# endregion
# ===========================================================================

# region ==== CHANGE AVATAR =================================================


@login_required
def change_avatar(request, avatar_id):
    avatarid = avatar_id
    profile = UserProfile.objects.get(user=request.user.id)
    if avatarid == 0:
        profile.avatar = None
    else:
        avatar = UserAvatar.objects.get(id=avatarid)
        profile.avatar = avatar
    profile.save()
    return redirect('userprofile')
# endregion
# ===========================================================================

# region ==== PAY THANKYOU ===================================================

@login_required
def pay_thankyou_view(request):
    if request.method == 'POST':
        payment_intent_secret = request.POST['payment_intent_secret']
        payment_intent_id = request.POST['payment_intent_id']
        payment_method_id = request.POST['payment_method_id']
        stripe_plan_id = settings.STRIPE_PLAN_ANNUALY_PRICE_ID
        auto_renew = request.POST['auto-renew-check']
        stripe.api_key = settings.STRIPE_SECRET_KEY

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
                payment_method=payment_method_id,
                customer=customer.id
            )
        else:
            stripe.PaymentIntent.modify(
                payment_intent_id,
                payment_method=payment_method_id
            )
            stripe.PaymentIntent.confirm(
                payment_intent_id
            )

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
    return redirect('userprofile')
# endregion
# ============================================================================

# region ==== ERROR HANDLING =================================================
def error_400_view(request, exception):
    return render(request, "400.html", status=400)

def error_404_view(request, exception):
    return render(request, "404.html", status=404)

def error_500_view(request):
    return render(request, '500.html', status=500)


# endregion
# ============================================================================