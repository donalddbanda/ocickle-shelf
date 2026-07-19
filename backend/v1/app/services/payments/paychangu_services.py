from datetime import datetime, timezone
from ..store_service import StoreService
from ...models.product import Product

def initiate_transaction(product: Product):
    tx_ref = f"{product.id}-{datetime.timestamp()}"

    payment_link = paychangu_client.initiate_payment(
        tx_ref=tx_ref,
        amount=product.amount,
        meta={
            "seller": StoreService.find_store(product.store_id).name,
            "name": product.name,
            "description": product.description
        }
    )
    response = payment_link["data"]["checkout_url"]
    return response