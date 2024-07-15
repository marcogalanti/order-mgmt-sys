from config import db, ma
import uuid

# Definizione del modello Order
class Order(db.Model):
    __tablename__ = 'OrderMgmtSys'
    id = db.Column(db.String(36), primary_key=True, nullable=False,  default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Numeric(10, 2), nullable=False)

    def __init__(self, name, description, price):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.price = price

# Definizione dello schema Order
class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order

# Inizializza lo schema
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
