from flask import Blueprint, render_template, send_file
from .models import Planet

blueprint = Blueprint('planets', __name__)

# @blueprint.route('/')
# def index():
#    return render_template('planets/index.html', planets=planets_data)

# @blueprint.route('/planets/<slug>')
# def planets(slug):
#     if slug in planets_data:
#         return '<h1>' + planets_data[slug]['name'] + '</h1><p>' + planets_data[slug]['diameter'] + '</p>'
#     else:
#        return 'That planet does not exist.'
    
@blueprint.route('/planets/<slug>')
def planets(slug):
   planet = Planet.query.filter_by(slug=slug).first()
   return render_template(planets/show.html, planet=planet)

@blueprint.route('/legal')
def legal():
  return send_file('static/downloads/legal.txt', as_attachment=True)
