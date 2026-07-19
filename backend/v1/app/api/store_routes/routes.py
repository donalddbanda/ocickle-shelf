from . import store_bp
from ...extensions import db
from flask import request, current_app, jsonify
from ...services.store_service import StoreService


@store_bp.route("/", method=["POST"])
def create_store(data):
    data = request.get_json()

    try:
        store = StoreService.create_store(data)

    except ValueError:
        db.session.rollback()
        return 400

    except Exception:
        db.session.rollback()
        return jsonify({
            "success": False,
            "message": "Failed to create store"
        }), 500

    return jsonify({
        "success": True,
        "message": "Store created successfully",
        "store": store.to_dict()
    }), 201

@store_bp.route("/<slug>", methods=["GET"])
def get_store_by_slug(slug):
    store = StoreService.find_store_by_slug(slug)
    return jsonify({
        "sucess": True,
        "message": "store retrieved",
        "data": store.to_public_dict()
    }), 200

@store_bp.route("/", methods=["GET"])
def get_stores():
    page = request.args.get("page", 1)
    stores = db.query.paginate(page=page, per_page=50, error_out=False)

    return jsonify({
        "success": True,
        "message": "stores retrieved successfully",
        "stores": [store.to_public_dict for store in stores],
        "has_next": stores.has_next,
        "has_prev": stores.has_prev,
        "page": stores.page,
        "pages": stores.pages,
        "next_page": stores.next_num,
        "prev_page": stores.prev_num,
        "total": stores.total
    }), 200

@store_bp.route("/<int:id>", methods=["GET"])
def get_store_by_id(id):
    store = StoreService.find_store(id)
    if not store:
        return jsonify({
            "success": False,
            "message": "Store not found"
        }), 404
    return store.to_public_dict()

@store_bp.route("/<int:id>/update", methods=["PATCH"])
def update_store(id):
    data = request.get_json()
    store = StoreService.find_store(id)

    try:
        StoreService.edit_store(id, data)

    except ValueError:
        db.session.rollback()
        return 400

    except Exception as e:
        db.session.rollback()
        return jsonify({
            "success": False,
            "message": "Failed to edit store"
        }), 500
    
    return jsonify({
        "success": True,
        "message": "store updated successfully",
        "store": store.to_public_dict()
    }), 200


@store_bp.route("/<int:id>/delete", methods=["POST"])
def delete_store(id):
    try:
        StoreService.delete_store(id)
    except Exception as e:
        db.session.rollback()
        current_app.logger(f"Failed to delete store {str(e)}")
        return jsonify({
            "success": False,
            "message": "Failed to delete store"
        }), 500