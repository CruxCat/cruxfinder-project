"""Server for climbing routes reviews app."""

from doctest import debug
from flask import (Flask, render_template, jsonify, request, flash, session, redirect)
from model import connect_to_db, db, Route, Rating, Climber
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

@app.route('/climber_profile/<climber_id>')
def climber_profile(climber_id):
    """Show climber profile page."""

    climber = crud.get_climber_by_id(climber_id)
    climber_reviews = crud.get_reviews_by_climber_id(climber_id)
    climber_ratings = crud.get_ratings_by_climber_id(climber_id)

    return render_template('climber_profile.html', climber=climber, climber_reviews=climber_reviews, climber_ratings=climber_ratings)

@app.route('/routes')
def all_routes():
    """View all climbing routes."""

    routes = crud.get_routes()

    return render_template('all_routes.html', routes=routes)

@app.route('/routes/<route_id>')
def show_route(route_id):
    """Show details on a climbing route."""

    route = crud.get_route_by_id(route_id)
    reviews = crud.get_reviews_by_route_id(route_id)
    average_rating = crud.get_average_rating_by_route_id(route_id)
    total_ratings = crud.total_rating_by_route_id(route_id)
 
    if session:
        climber = session["climber_id"]
        ratings = crud.check_ratings(route_id, climber)
    else:
        climber = None
        ratings = None

    return render_template('route_details.html', route_id=route_id, route=route, reviews=reviews, average_rating=average_rating, total_ratings=total_ratings, ratings=ratings)

@app.route('/climbers', methods=["POST"])
def register_climber():
    """Create a new climber."""

    name = request.form.get("name")
    location = request.form.get("location")
    goals = request.form.get("goals")
    email = request.form.get("email")
    password = request.form.get("password")

    climber = crud.get_climber_by_email(email)
    if climber:
        flash("That email is already taken. Try logging in below.")
    else:
        climber = crud.create_climber(name, location, goals, email, password)
        db.session.add(climber)
        db.session.commit()
        flash("Account created successfully. Please log in below.")

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
        session["climber_id"] = climber.climber_id
        flash(f"Logged in! Welcome back, {climber.name}!")

    return redirect('/')

@app.route('/logout')
def logout():
    """Allow the climber to log out."""

    session.pop('climber_email')
    session.pop('climber_id')
    flash(f"You have successfully logged out.")
    return redirect('/')

@app.route("/routes/<route_id>/ratings", methods=["POST"])
def create_rating(route_id):
    """Create a new rating for a climbing route."""

    logged_in_email = session.get("climber_email")
    rating_score = request.form.get("rating")

    if logged_in_email is None:
        flash("You must log in to rate a climbing route.")
    else:
        climber = crud.get_climber_by_email(logged_in_email)
        route = crud.get_route_by_id(route_id)

        rating = crud.create_rating(climber, route, int(rating_score))
        db.session.add(rating)
        db.session.commit()

        flash(f"You rated this climb {rating_score} out of 5 stars.")

    return redirect(f"/routes/{route_id}")

@app.route("/update_rating", methods=["POST"])
def update_rating():

    rating_id = request.json["rating_id"]
    updated_score = request.json["updated_score"]
    crud.update_rating(rating_id, updated_score)
    db.session.commit()

    return updated_score

@app.route("/routes/<route_id>/reviews", methods=["POST"])
def create_review(route_id):
    """Create a new review for the specified route."""

    logged_in_email = session.get("climber_email")
    content = request.form.get("review")
    date = request.form.get("date")
    
    if logged_in_email is None:
        flash("You must log in to review a climbing route.")
    elif not date:
        flash("Error: you must enter a date you climbed the route.")
    else: # if logged_in_email exists
        climber = crud.get_climber_by_email(logged_in_email)
        route = crud.get_route_by_id(route_id)

        review = crud.create_review(route, climber, date, content)
        db.session.add(review)
        db.session.commit()

        flash(f"Thanks for your review of this climb!")

    return redirect(f"/routes/{route_id}")

@app.route('/api/routes')
def route_info():
    """JSON information about routes for map"""

    routes = [
        {
            "id": route.route_id,
            "routeName": route.route,
            "grade": route.grade,
            "latitude": route.latitude,
            "longitude": route.longitude,
            "picture": route.picture_path
        }
        for route in Route.query.all()
    ]

    return jsonify(routes)

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    app.debug = True
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True) 