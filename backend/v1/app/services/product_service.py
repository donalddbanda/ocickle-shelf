from ..models.product import Product
from ..models.store import Store
from ..services.store_service import StoreService


class ProductService:

    @staticmethod
    def can_add_product(store: Store):
        return store.products < 5
    
    # @staticmethod
    # def edit_product(id, data):
    #     if len(data["attachments"]) > 6:
    #         raise ValueError("You can only upload 6 media files")

    #     product = ProductService.find_product(id)

    #     if product:
    #         product.name = data.get("name") if data["name"] else product.name
    #         product.description = data.get("description") if data["description"] else product.description
    #         product.amount = data.get("amount") if data["amount"] else product.amount
    #         product.payment_link = data.get("payment_link") if data["payment_link"] else product.payment_link
    #         product.attachments = data.get("attachments") if data["attachments"] else product.attachament
    #         product.updated_at = datetime.now(timezone.utc)

    #         db.session.commit()

    #     return product
    
    @staticmethod
    def find_product(product_id: Product.id):
        return Product.query.get(product_id)
    
    # def delete_product(id):
    #     product = ProductService.find_product(id)

    #     db.session.delete(product)
    #     db.session.commit()

    #     return "product deleted"