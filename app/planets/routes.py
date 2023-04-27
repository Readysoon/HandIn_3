from flask import Blueprint, render_template, send_file, request, current_app, redirect, url_for
from .models import Planet
from app.extensions.database import db

blueprint = Blueprint('planets', __name__)


@blueprint.route('/planets')
@blueprint.route('/')
def planets_all():
   page_number = request.args.get('page', 1, type=int)
   print('=> Page number:', page_number)
   #changed to following line according to the pagination chapter from
   # "   all_planets = Planet.query.all()" to 
   planets_pagination = Planet.query.paginate(page=page_number, per_page=current_app.config['PLANETS_PER_PAGE'])
   # and this line from '   return render_template('cookies/index.html', planets=all_planets)' to
   return render_template('planets/index.html', planets_pagination=planets_pagination)
    
@blueprint.route('/planets', methods=['POST'])
def add_planet():
    # Get the data from the request form
    name = request.form.get('name')
    diameter = request.form.get('diameter')
    price = request.form.get('price')

    # Create a new planet instance
    new_planet = Planet(name=name, diameter=diameter, price=price)

    # Add the new planet to the database
    db.session.add(new_planet)
    db.session.commit()

    # Redirect the user to the page for the newly created planet
    return redirect(url_for('planets.planets', id=new_planet.id))

@blueprint.route('/planetsedit/<int:id>', methods=['GET', 'POST'])
def edit_planet(id):
    planet = Planet.query.get(id)
    if request.method == 'POST':
        planet.name = request.form['name']
        planet.diameter = request.form['diameter']
        planet.mass = request.form['mass']
        planet.price = request.form['price']
        db.session.commit()
        return redirect(url_for('planets.planets', id=id))
    return render_template('planets/edit.html', planet=planet)

@blueprint.route('/planetsdelete/<int:id>', methods=['POST'])
def delete_planet(id):
    planet = Planet.query.get(id)
    if planet is not None:
        db.session.delete(planet)
        db.session.commit()
    return redirect(url_for('planets.planets_all'))

# grabs the first entry of the database based on codecookies -> CRUD 
@blueprint.route('/planets/<id>')
def planets(id):
   planet = Planet.query.filter_by(id=id).first_or_404()
   return render_template('planets/show.html', planet=planet)

@blueprint.route('/legal')
def legal():
  return send_file('static/downloads/legal.txt', as_attachment=True)

@blueprint.route('/run-seed')
def run_seed():
    if not Planet.query.filter_by(slug='mercury').first():
        import app.scripts.seed
        return 'Database seed completed!'
    else:
        return 'Nothing to run.'
    

