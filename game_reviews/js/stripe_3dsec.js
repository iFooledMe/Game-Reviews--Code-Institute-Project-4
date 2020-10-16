function card(stripe_publishable_key, pi_secret) {
    window.addEventListener('DOMContentLoaded', (event) => {
        var stripe = Stripe(stripe_publishable_key)

        stripe.confirmCardPayment(pi_secret).then(function(result) {

            if (result.error) {
                $('#3ds_result').text('Error!');
                $('#3ds_result').addClass('text-danger');
            }
            else {
                $('#3ds_result').text('Thank you for your payment!');
                $('#3ds_result').addClass('text-success');
            }
        });
    }); //Dom Content Loaded
}
