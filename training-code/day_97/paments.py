import stripe

stripe.api_key = "your_stripe_secret_key"

def create_payment_intent(amount: int, currency: str = 'usd'):
    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency=currency,
    )
    return intent
