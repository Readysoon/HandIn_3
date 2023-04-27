from app.extensions.database import db, CRUDMixin

class Planet(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(80))
    diameter = db.Column(db.Numeric(10,2))
    mass = db.Column(db.Numeric(10,2))
    price = db.Column(db.Numeric(10,2))

def test_planet_update(client):
    # update planet's properties
    planet = Planet(slug='pluto', name='Pluto', diameter=2376)
    db.session.add(planet)
    db.session.commit()

    planet.name = "Neptun"
    planet.save()

    updated_planet = Planet.query.filter_by(slug='Pluto').first()
    assert updated_planet.name == 'Pluto'


# in the CRUD Tutorial first 'chocolate chip' then 'butter' is used?
def test_planet_delete(client):
    # deletes planet
    planet = Planet(slug='pluto', name="Pluto", diameter=2376)
    db.session.add(planet)
    db.session.commit()

    planet.delete()

    deleted_planet = Planet.query.filter_by(slug='pluto').first()
    assert deleted_planet is None

