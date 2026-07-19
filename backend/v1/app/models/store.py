from ..extensions import db
from datetime import datetime, timezone


class Store(db.Column):
    __tablename__ = "store"

    id = db.Column(db.Integer, primary_key=True)
    header_img = db.Column(db.String(250), nullalble=False)
    name = db.Column(db.String(100), nullable=False, index=True)
    description = db.Column(db.Text, nullable=True)
    slug = db.Column(db.String(40), nullable=False, unique=True, index=True)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), index=True)
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), index=True)

    # foreign keys
    owner_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))

    # relationships
    products = db.relationship("Product", backref="products", lazy="dynamic")

    def __repr__(self):
        return f"<Store {self.id}: {self.name}, {self.slug}>"

    def to_dict(self):
        return {
            "id": self.user_id,
            "name": self.name,
            "slug": self.slug,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "owner_id": self.owner_id,
            "products": self.products
        }
    def to_public_dict(self):
        return {
            "id": self.user_id,
            "name": self.name,
            "slug": self.slug,
            "products": self.products
        }