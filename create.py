from application import db
from application.models import Users, Product, Order_line, Order

db.drop_all()
db.create_all()
