"""CRUD operations for cruxfinder app."""

from model import db, Climber, Route, Review, Rating, connect_to_db

def create_climber(name, email, password):
    """Create and return a new user."""

    climber = Climber(name = name, email=email, password=password)

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

def create_review(climber, date, content):
    """Create and return a new review."""

    review = Review(climber=climber, date=date, content=content)

    return review

def create_rating(climber, route, stars):
    """Create and return a new rating."""

    rating = Rating(climber=climber, route=route, stars=stars)

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
