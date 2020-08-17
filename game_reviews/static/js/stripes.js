function card(stripe_publishable_key, customer_email) {
    window.addEventListener('DOMContentLoaded', (event) => {
        console.log(stripe_publishable_key);
        console.log(customer_email);
        var stripe = Stripe(stripe_publishable_key);
        var elements = stripe.elements();

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
    }); //Dom Content Loaded
}
