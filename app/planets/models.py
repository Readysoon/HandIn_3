from app.extensions.database import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(80))
    diameter = db.Column(db.Numeric(10,2))
    picture_url = db.Column(db.String(260))