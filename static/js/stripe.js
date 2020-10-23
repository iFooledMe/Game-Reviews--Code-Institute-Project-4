// This entire script is taken from:
// Django Lessons @ https://www.youtube.com/watch?time_continue=110&v=Bq5lR5WQNOw&feature=emb_logo

function card(stripe_publishable_key, customer_email) {
    window.addEventListener('DOMContentLoaded', (event) => {
        var stripe = Stripe(stripe_publishable_key);
        var elements = stripe.elements();

        // Style form card form
        var style = {
            base: {
                color: '#32325d',
                fontFamily: '"Roboto", sans-serif',
                fontSmoothing: 'antialiased',
                fontSize: '16px',
                '::placeholder': {
                    color: '#aab7c4',
                },
            },
            invalid: {
                color: '#fa755a',
                iconColor: '#fa755a',
            },
        };

        // Creates card form in the element
        var card = elements.create('card', { style: style });
        card.mount('#card-element');

        card.addEventListener('change', function (event) {
            var displayError = document.getElementById('card-errors');
            if (event.error) {
                displayError.textContent = event.error.message;
            } else {
                displayError.textContent = '';
            }
        });

        //Handle form submission.
        var form = document.getElementById('payment-form');
        form.addEventListener('submit', function (event) {
            event.preventDefault();

            stripe.createToken(card).then(function (result) {
                if (result.error) {
                    //inform the user if there was an error
                    var errorElement = document.getElementById('card-errors');
                    errorElement.textContent = result.error.message;
                }
                // <--- Create payment method start
                else {
                    stripe
                        .createPaymentMethod({
                            type: 'card',
                            card: card,
                            billing_details: {
                                email: customer_email,
                            },
                        })
                        .then(function (payment_method_result) {
                            if (payment_method_result.error) {
                                var errorElement = document.getElementById(
                                    'card-errors'
                                );
                                errorElement.textContent =
                                    payment_method_result.error.message;
                            } else {
                                var form = document.getElementById(
                                    'payment-form'
                                );
                                var hiddenInput = document.createElement(
                                    'input'
                                );

                                hiddenInput.setAttribute('type', 'hidden');
                                hiddenInput.setAttribute(
                                    'name',
                                    'payment_method_id'
                                );
                                hiddenInput.setAttribute(
                                    'value',
                                    payment_method_result.paymentMethod.id
                                );

                                form.appendChild(hiddenInput);

                                form.submit();
                            }
                        });
                }
            }); // Create Payment Method end --->
        }); // form.addEventListener end
    }); //Dom Content Loaded
}
