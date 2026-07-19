from ..extensions import db
from ..models.store import Store
from datetime import datetime, timezone

class StoreService:

    @staticmethod
    def find_store(id):
        return Store.query.get(id)

    @staticmethod
    def find_store_by_slug(slug):
        return Store.query.filter_by(slug=slug).first()
    
    @staticmethod
    def create_store(data):
        if not StoreService.find_store_by_slug(data["slug"]):
            raise ValueError("Slug already taken")

        if len(data["slug"]) > 40:
            raise ValueError("Slug should be 40 characters or less")

        if len(data["name"]) > 100:
            raise ValueError("Store name should be 100 characters or less")

        store = Store(
            name=data["name"],
            slug=data["slug"],
            description=data["description"],
            header_img=data["header_img"]
        )

        db.session.add(store)
        db.session.commit()

        return store

    @staticmethod
    def edit_store(store_id, data):
        store = StoreService.find_store(store_id)

        if not store:
            return "store not found"

        if len(data["slug"]) > 40:
            raise ValueError("Slug should be 40 characters or less")
        
        if StoreService.find_store_by_slug(data["slug"]):
            raise ValueError("Store slug already taken")

        if len(data["name"]) > 100:
            raise ValueError("Store name should be 100 characters or less")

        store.name=data.get("name") if data["name"] else store.name,
        store.slug=data.get("slug") if data["slug"] else store.slug,
        store.description=data.get("description") if data["description"] else store.description,
        store.header_img=data.get("header_img") if data["header_img"] else store.header_img
        store.updated_at = datetime.now(timezone.utc)

        db.session.commit()

        return store

    @staticmethod
    def delete_store(id):
        store = StoreService.find_store(id)
        
        if not store:
            return "store not found"
        
        db.session.delete(store)
        db.session.commit()