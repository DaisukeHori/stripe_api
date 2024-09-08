from fastapi import APIRouter, Query, HTTPException, Depends
from app.models.stripe_models import (
    CustomerResponse, SubscriptionResponse, InvoiceResponse,
    PaymentResponse, ProductResponse, StripeError
)
from app.services.stripe_service import (
    get_customers_by_email, get_subscriptions, get_invoices,
    get_payments, get_products
)
from app.core.config import settings
from app.core.auth import verify_auth_key
import stripe
import logging

router = APIRouter()
logger = logging.getLogger("stripe_api")

def handle_stripe_error(e: stripe.error.StripeError):
    error_msg = f"Stripe API error: {str(e)}"
    logger.error(error_msg)
    if isinstance(e, stripe.error.RateLimitError):
        raise HTTPException(status_code=429, detail=error_msg)
    elif isinstance(e, stripe.error.InvalidRequestError):
        raise HTTPException(status_code=400, detail=error_msg)
    elif isinstance(e, stripe.error.AuthenticationError):
        raise HTTPException(status_code=401, detail=error_msg)
    elif isinstance(e, stripe.error.APIConnectionError):
        raise HTTPException(status_code=503, detail=error_msg)
    else:
        raise HTTPException(status_code=500, detail=error_msg)

@router.get("/customers/{email}", response_model=CustomerResponse, responses={400: {"model": StripeError}, 401: {"model": StripeError}})
def get_customers(email: str, auth_key: str = Depends(verify_auth_key)):
    try:
        customers = get_customers_by_email(email)
        return CustomerResponse(customers=customers)
    except stripe.error.StripeError as e:
        handle_stripe_error(e)

@router.get("/subscriptions/{email}", response_model=SubscriptionResponse, responses={400: {"model": StripeError}, 401: {"model": StripeError}})
def get_customer_subscriptions(email: str, limit: int = Query(50, le=settings.MAX_LIMIT), auth_key: str = Depends(verify_auth_key)):
    try:
        customers = get_customers_by_email(email)
        all_subscriptions = []
        for customer in customers:
            subscriptions = get_subscriptions(customer.id, limit)
            all_subscriptions.extend(subscriptions)
        return SubscriptionResponse(subscriptions=all_subscriptions)
    except stripe.error.StripeError as e:
        handle_stripe_error(e)

@router.get("/invoices/{email}", response_model=InvoiceResponse, responses={400: {"model": StripeError}, 401: {"model": StripeError}})
def get_customer_invoices(email: str, limit: int = Query(50, le=settings.MAX_LIMIT), auth_key: str = Depends(verify_auth_key)):
    try:
        customers = get_customers_by_email(email)
        all_invoices = []
        for customer in customers:
            invoices = get_invoices(customer.id, limit)
            all_invoices.extend(invoices)
        return InvoiceResponse(invoices=all_invoices)
    except stripe.error.StripeError as e:
        handle_stripe_error(e)

@router.get("/payments/{email}", response_model=PaymentResponse, responses={400: {"model": StripeError}, 401: {"model": StripeError}})
def get_customer_payments(email: str, limit: int = Query(50, le=settings.MAX_LIMIT), auth_key: str = Depends(verify_auth_key)):
    try:
        customers = get_customers_by_email(email)
        all_payments = []
        for customer in customers:
            payments = get_payments(customer.id, limit)
            all_payments.extend(payments)
        return PaymentResponse(payments=all_payments)
    except stripe.error.StripeError as e:
        handle_stripe_error(e)

@router.get("/products/{email}", response_model=ProductResponse, responses={400: {"model": StripeError}, 401: {"model": StripeError}})
def get_customer_products(email: str, limit: int = Query(50, le=settings.MAX_LIMIT), auth_key: str = Depends(verify_auth_key)):
    try:
        customers = get_customers_by_email(email)
        all_products = set()
        for customer in customers:
            subscriptions = get_subscriptions(customer.id, limit)
            for subscription in subscriptions:
                products = get_products(subscription.items.data)
                all_products.update(products)
        return ProductResponse(products=list(all_products))
    except stripe.error.StripeError as e:
        handle_stripe_error(e)
