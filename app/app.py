from . import planets, orders
from flask import Flask
from app.extensions.database import db, migrate


def create_app():
  app = Flask(__name__)
  app.config.from_object('app.config')

  register_blueprints(app)
  register_extensions(app)

  return app

#Blueprints
def register_blueprints(app: Flask):
  app.register_blueprint(planets.routes.blueprint)
  app.register_blueprint(orders.routes.blueprint)




def register_extensions(app: Flask):
  db.init_app(app)
  migrate.init_app(app, db, compare_type=True)