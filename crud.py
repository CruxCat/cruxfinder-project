"""CRUD operations for cruxfinder app."""

from model import db, Climber, Route, Review, Rating, connect_to_db

def create_climber(name, location, goals, email, password):
    """Create and return a new user."""

    climber = Climber(name = name, location = location, goals = goals, email = email, password = password)

    return climber

def get_climber_by_id(climber_id):
    """Return a climber by primary key."""

    return Climber.query.get(climber_id)

def get_climber_by_email(email):
    """Return a climber by email."""

    return Climber.query.filter(Climber.email == email).first()

def create_route(route, grade, latitude, longitude, picture_path):
    """Create and return a new route."""

    route = Route(route=route, grade=grade, latitude=latitude, longitude=longitude, picture_path=picture_path)

    return route

def get_routes():
    """Return a list of routes."""

    return Route.query.all()

def get_route_by_id(route_id):
    """Get a route database object by primary key."""

    return Route.query.get(route_id)

def create_review(route, climber, date, content):
    """Create and return a new review."""

    review = Review(route=route, climber=climber, date=date, content=content)

    return review

def get_reviews_by_route_id(route_id):
    """Get all the reviews by route id."""

    return Review.query.filter(Review.route_id == route_id).all()

def create_rating(climber, route, stars):
    """Create and return a new rating."""

    rating = Rating(climber=climber, route=route, stars=stars)

    return rating

def update_rating(rating_id, new_stars):
    """Update a rating given rating_id and the updated stars."""

    rating = Rating.query.get(rating_id)
    rating.stars = new_stars

def get_average_rating_by_route_id(route_id):
    """Get average of the start ratings by route_id."""

    average_rating = Rating.query.filter(Rating.route_id == route_id).all().average()

    return average_rating

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
