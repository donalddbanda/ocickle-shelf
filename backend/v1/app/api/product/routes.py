from . import product_bp
from ...extensions import db
from ...services.store_service import StoreService
from ...services.product_service import ProductService
from ...models.product import Product
from flask import jsonify, request, current_app
from app.utils.exceptions import StoreNotFoundError, ProductNotFoundError


@product_bp.route("/<int:store_id>", methods=["POST"])
def create_product(store_id):

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "data not provided."
        }), 400

    name = data["name"]
    description = data["description"]
    amount = data["amount"]
    payment_link = data["payment_link"]
    attachments = data["attachments"]

    if attachments and len(attachments) > 5:
        return jsonify({
            "success": False,
            "message": "Attachments exceed 5."
        }), 400

    if not all([name, amount, payment_link, attachments]):
        return jsonify({
            "success": False,
            "message": "name, amount, payment link, and attachments not provided."
        }), 400

    store = StoreService.find_store(store_id)
    if not store:
        raise StoreNotFoundError("Invalid store.")

    if not ProductService.can_add_product(store):
        return "Maximum products limit reached."

    product = Product(
        name=name,
        description=description,
        amount=amount,
        payment_link=payment_link,
        attachments=attachments,
        store_id=store_id
    )

    try:
        db.session.add(product)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger(f"Failed to create product: {str(e)}")
        return jsonify({
            "success": False,
            "message": "Failed to create product."
        }), 500

    return jsonify({
        "success": True,
        "message": "Product created.",
        "product": product.to_dict()
    }), 201


@product_bp.route("/<int:store_id>/<int:product_id>", methods=["PATCH"])
def update_product(store_id, product_id):

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "data not provided."
        }), 400
    product = ProductService.find_product(product_id)
    if not product:
        raise ProductNotFoundError("Invalid product.")

    store = StoreService.find_store(store_id)
    if not store or product.store_id!=store_id:
        raise StoreNotFoundError("Invalid store.")

    product.name = data.get("name", product.name)
    product.description = data.get("description", product.description)
    product.amount = data.get("amount", product.amount)
    product.payment_link = data.get("payment_link", product.payment_link)
    product.attachments = data.get("attachments", product.attachaments)

    if data.get("attachments") and len(data.get("attachments")) > 5:
        return jsonify({
            "success": False,
            "message": "Attachments exceed 5."
        }), 400

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger(f"Failed to edit product: {str(e)}")
        return jsonify({
            "success": False,
            "message": "Failed to edit product."
        }), 500

    return jsonify({
        "success": True,
        "message": "Product edited.",
        "product": product.to_dict()
    }), 200


@product_bp.route("/<int:store_id>/", methods=["GET"])
def get_store_products(store_id):
    store = StoreService.find_store(store_id)
    if not store:
        raise StoreNotFoundError("Invalid store.")
    
    page = request.args.get("page", 1)
    per_page = 15 if request.args.get("per_page") > 15 else request.args.get("per_page", 15)

    products_data = store.query.paginate(per_page=per_page, error_out=False, page=page)
    
    return jsonify({
        "success": True,
        "message": "Product created successfully.",
        "data": {
            "page": page,
            "total": products_data.total,
            "has_next": products_data.has_next,
            "has_prev": products_data.has_prev,
            "prev_page": products_data.prev_num,
            "next_page": products_data.next_num,
            "products": [product.to_dict() for product in products_data.items]
            }
    }), 200

@product_bp.route("/<int:product_id>/", methods=["GET"])
def get_product(product_id):
    product = ProductService.find_product(product_id)
    if not product:
        raise ProductNotFoundError("Invalid product.")
    
    return jsonify({
        "success": True,
        "message": "Product retrieved successfully.",
        "product": product.to_dict()
    }), 200

@product_bp.route("/<int:product_id>", methods=["DELETE"])
def delete_product(product_id: int):
    product = ProductService.find_product(product_id)
    if not product:
        raise ProductNotFoundError("Invalid product.")

    try:db.session.delete(product)
    except Exception as e:
        db.session.rollback()
        current_app.logger(f"Failed to delete product: {str(e)}")
        return jsonify({
            "success": False,
            "message": "Failed to delete product."
        }), 500
    
    return jsonify({
        "success": True,
        "message": "Product deleted."
    }), 200