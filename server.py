"""Server for climbing routes reviews app."""

from doctest import debug
from flask import (Flask, render_template, request, flash, session, redirect)

from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "early_secret_key"
app.jinja_env.undefined = StrictUndefined

# Create home page
@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/login')
def login():
    """View login page."""

    return render_template('login.html')

@app.route('/routes')
def all_routes():
    """View all routes."""

    routes = crud.get_routes()

    return render_template('all_routes.html', routes=routes)

@app.route('/routes/<route_id>')
def show_route(route_id):
    """Show details on a particular climbing route."""

    route = crud.get_route_by_id(route_id)

    return render_template('route_details.html', route=route)

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True) 