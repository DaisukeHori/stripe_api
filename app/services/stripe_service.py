import stripe
from functools import lru_cache
from app.core.config import settings
import logging
from typing import List, Dict, Any

logger = logging.getLogger("stripe_api")

stripe.api_key = settings.STRIPE_API_KEY

@lru_cache(maxsize=100)
def get_customers_by_email(email: str) -> List[stripe.Customer]:
    logger.info(f"Fetching customers for email: {email}")
    return list(stripe.Customer.list(email=email).auto_paging_iter())

def get_subscriptions(customer_id: str, limit: int) -> List[Dict[str, Any]]:
    logger.info(f"Fetching subscriptions for customer: {customer_id}")
    return stripe.Subscription.list(customer=customer_id, limit=limit).data

def get_invoices(customer_id: str, limit: int) -> List[Dict[str, Any]]:
    logger.info(f"Fetching invoices for customer: {customer_id}")
    return stripe.Invoice.list(customer=customer_id, limit=limit).data

def get_payments(customer_id: str, limit: int) -> List[Dict[str, Any]]:
    logger.info(f"Fetching payments for customer: {customer_id}")
    return stripe.PaymentIntent.list(customer=customer_id, limit=limit).data

def get_products(subscription_items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    logger.info("Fetching products")
    product_ids = set(item.price.product for item in subscription_items)
    return [stripe.Product.retrieve(product_id) for product_id in product_ids]