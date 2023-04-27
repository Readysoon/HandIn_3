from flask import Blueprint, render_template, request, current_app
from app.planets.models import Planet
from flask_login import login_required

# from .services

blueprint = Blueprint("orders", __name__)


@blueprint.get("/checkout")
@login_required
def get_checkout():
    planets = Planet.query.all()
    return render_template("orders/order.html", planets=planets)


@blueprint.post("/checkout")
def post_checkout():
    planets = Planet.query.all()
    return render_template("orders/order.html", planets=planets)


# tried to do the validation but 'create_order' does not work, seems I have to create it somewhere first

# @blueprint.post('/checkout')
# def post_checkout():
#     planets = Planet.query.all()

#     if not all([
#       request.form.get('name'),
#       request.form.get('street'),
#       request.form.get('city'),
#       request.form.get('state'),
#       request.form.get('zip'),
#       request.form.get('country'),
#       ]):
#         raise Exception('Please fill out all the address fields.')

#     create_order(request.form, planets)
#     return render_template('orders/new.html', planets=planets)
#   except Exception as error_message:
#     error = error_message or 'An error occured while processing your order. Please make sure to enter valid data.'

#     current_app.logger.info(f'Error creating an order: {error}')

#     return render_template('orders/new.html',
#          planets=planets,
#          error='An error occured while processing your order. Please make sure to enter valid data.'
#     )
