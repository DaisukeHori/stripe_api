from pydantic import BaseModel, EmailStr
from typing import List, Dict, Any

class StripeError(BaseModel):
    detail: str

class CustomerResponse(BaseModel):
    customers: List[Dict[str, Any]]

class SubscriptionResponse(BaseModel):
    subscriptions: List[Dict[str, Any]]

class InvoiceResponse(BaseModel):
    invoices: List[Dict[str, Any]]

class PaymentResponse(BaseModel):
    payments: List[Dict[str, Any]]

class ProductResponse(BaseModel):
    products: List[Dict[str, Any]]