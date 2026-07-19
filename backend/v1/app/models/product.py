from ..extensions import db


class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, index=True)
    description = db.Column(db.Text, nullable=True)
    amount = db.Column(db.Numeric(10,2), nullalbe=False, index=True)
    payment_link = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), index=True)
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), index=True)

    # relationships
    attachments = db.relationship("Attachments", lazy="dynamic", backref="attachments")

    # foreign keys
    store_id = db.Column(db.Integer, db.ForeignKey("store.id"))

    def __repr__(self):
        return f"<Product: {self.id}, {self.name}, {self.amount}>"
    
    def to_dict(self):
        return {
            "id": {self.id},
            "name": {self.name},
            "description": {self.description},
            "amount": {self.amount},
            "created_at": {self.created_at},
            "updated_at": {self.updated_at},
            "attacments": {self.attachments}
        }