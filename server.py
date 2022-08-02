"""Server for climbing routes reviews app."""

from doctest import debug
from flask import (Flask, render_template, request, flash, session, redirect)

from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "early_secret_key"
app.jinja_env.undefined = StrictUndefined


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

@app.route('/climbers', methods=["POST"])
def register_climber():
    """Create a new climber."""

    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    climber = crud.get_climber_by_email(email)
    if climber:
        flash("Cannot create an account with that email. That email is already registered.")
    else:
        climber = crud.create_climber(name, email, password)
        db.session.add(climber)
        db.session.commit()
        flash("Account created successfully. Please log in.")

    return redirect('/')

@app.route('/climber_login', methods=["POST"])
def login_climber():
    """Process climber login."""

    email = request.form.get("email")
    password = request.form.get("password")

    climber = crud.get_climber_by_email(email)
    if not climber or climber.password != password:
        flash("The email or password you entered was incorrect. Please try again.")
    else:
        # Log in user by storing the user's email in session
        session["climber_email"] = climber.email
        flash(f"Logged in! Welcome back, {climber.name}!")

    return redirect('/')

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True) 