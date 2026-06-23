from extensions import db
from datetime import datetime, timezone


class User(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.Integer, nullable=False, index=True)
    name = db.Column(db.String(500), nullable=False)

    stores = db.relationship("Store", backref="stores", lazy="dynamic")

    def __repr__(self):
        return f"<User: {self.user_id}, {self.name}>"

    def to_dict(self):
        return {
            "id": self.user_id,
            "name": self.name,
        }


class Store(db.Column):
    __tablename__ = "store"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)

    owner_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))


class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    amount = db.Column(db.Numeric(10,2), nullalbe=False, index=True)
    quantity = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, default=daetime.now(timezone.utc), index=True)
    updated_at = db.Column(db.DateTime, default=daetime.now(timezone.utc), index=True)

    attachments = db.relationship("Attachments", lazy="dynamic", backref="attachments")

    def __repr__(self):
        return f"<Product: {self.id}, {self.name}, {self.amount}>"
    
    def to_string(self):
        return {
            "id": {self.id},
            "name": {self.name},
            "description": {self.description},
            "amount": {self.amount},
            "created_at": {self.created_at},
            "updated_at": {self.updated_at},
            "attacments": {self.attachments}
        }


class Attachments(db.Model):
    __tablename__ = "attachments"


    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.JSON, nullable=False)

    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
