from flask import Blueprint, render_template, send_file, request, current_app
from .models import Planet

blueprint = Blueprint('planets', __name__)

# took "@blueprint.route('/')" and moved it to def planets_all() and then commented out the following code:
# def index():
#    planets_data = Planet.query.all()
#    return render_template('planets/index.html', planets=planets_data)

# @blueprint.route('/planets/<slug>')
# def planets(slug):
#     if slug in planets_data:
#         return '<h1>' + planets_data[slug]['name'] + '</h1><p>' + planets_data[slug]['diameter'] + '</p>'
#     else:
#        return 'That planet does not exist.'

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
    

