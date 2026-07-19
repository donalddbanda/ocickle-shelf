from app import create_app
from app.extensions import db
from app.models.user import User
from app.models.store import Store
from app.models.product import Product
from app.models.attachment import Attachments


app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "User": User,
        "Product": Product,
        "Store": Store,
        "Attachements": Attachments
    }

app.run(debug=False)