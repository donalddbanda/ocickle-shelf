from ..extensions import db

class Attachments(db.Model):
    __tablename__ = "attachments"


    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.JSON, nullable=False)

    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
