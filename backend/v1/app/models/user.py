from ..extensions import db

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
            "slug": self.slug
        }
