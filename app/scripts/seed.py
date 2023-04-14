from app.app import create_app
from app.planets.models import Planet
from app.extensions.database import db

if __name__ == "__main__":
    app = create_app()
    app.app_context().push()

planets_data = {
  'mercury' : {'name': 'Mercury', 'diameter': 4879},
  'venus' : {'name': 'Venus', 'diameter': 12104},
  'earth' : {'name': 'Earth', 'diameter': 12756},
  'mars' : {'name': 'Mars', 'diameter': 6792},
  'jupiter' : {'name': 'Jupiter', 'diameter': 142984},
  'saturn' : {'name': 'Saturn', 'diameter': 120536},
  'uranus' : {'name': 'Uranus', 'diameter': 51118},
  'neptun' : {'name': 'Neptun', 'diameter': 49528},
}

for slug, planet in planets_data.items():
    new_planet = Planet(slug=slug, name=planet['name'], diameter=planet['diameter'])
    db.session.add(new_planet)

db.session.commit()

# @blueprint.route('run-seed')
# def run_seed():
#     if not Planet.query.filter_by(slug='mercury').first():
#         import app.scripts.seed
#         return 'Database seed completed!'
#     else:
#         return 'Nothing to run.'


