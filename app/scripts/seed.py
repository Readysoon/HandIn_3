from app.app import create_app
from app.planets.models import Planet
from app.extensions.database import db

if __name__ == "__main__":
    app = create_app()
    app.app_context().push()

planets_data = {
    "mercury": {"name": "Mercury", "diameter": 4879, "mass": 3.285, "price": 100},
    "venus": {"name": "Venus", "diameter": 12104, "mass": 4.867, "price": 200},
    "earth": {"name": "Earth", "diameter": 12756, "mass": 5.972, "price": 350},
    "mars": {"name": "Mars", "diameter": 6792, "mass": 6.39, "price": 150},
    "jupiter": {"name": "Jupiter", "diameter": 142984, "mass": 1.898, "price": 450},
    "saturn": {"name": "Saturn", "diameter": 120536, "mass": 5.683, "price": 750},
    "uranus": {"name": "Uranus", "diameter": 51118, "mass": 8.681, "price": 800},
    "neptun": {"name": "Neptun", "diameter": 49528, "mass": 11.0, "price": 500},
}

for slug, planet in planets_data.items():
    new_planet = Planet(
        slug=slug,
        name=planet["name"],
        diameter=planet["diameter"],
        mass=planet["mass"],
        price=planet["price"],
    )
    db.session.add(new_planet)

db.session.commit()

# @blueprint.route('run-seed')
# def run_seed():
#     if not Planet.query.filter_by(slug='mercury').first():
#         import app.scripts.seed
#         return 'Database seed completed!'
#     else:
#         return 'Nothing to run.'
