from app.extensions.database import db, CRUDMixin
from datetime import datetime


class Order(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    address_id = db.Column(db.Integer, db.ForeignKey("address.id"))
    planet_orders = db.relationship("PlanetOrder", backref="order", lazy=True)


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    street = db.Column(db.String(80))
    city = db.Column(db.String(80))
    state = db.Column(db.String(80))
    zip = db.Column(db.String(80))
    country = db.Column(db.String(80))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class PlanetOrder(db.Model):
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"), primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"), primary_key=True)
    number_of_planets = db.Column(db.Integer)
