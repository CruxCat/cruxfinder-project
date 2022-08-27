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

def check_reviews(route_id, climber_id):
    """Get all the reviews for a given route_id and climber_id to check if the climber has already written a review for a route."""

    check_reviews = db.session.query(Review.review_id).filter(Review.route_id==route_id, Review.climber_id==climber_id).all()

    return check_reviews

def get_reviews_by_route_id(route_id):
    """Get all the review content for a given route by route id."""

    reviews = db.session.query(Climber.name, Review.date, Review.content).join(Review).filter(Review.route_id == route_id).all()

    return reviews

def create_rating(climber, route, stars):
    """Create and return a new rating."""

    rating = Rating(climber=climber, route=route, stars=stars)

    return rating

def update_rating(rating_id, new_score):
    """Update a rating"""
    rating = Rating.query.get(rating_id)
    rating.stars = new_score

def check_ratings(route_id, climber_id):
    """Get all ratings for a given route_id and climber_id to check if a climber has already rated a route."""
    check_ratings = db.session.query(Rating.rating_id, Rating.stars).filter(Rating.route_id==route_id, Rating.climber_id==climber_id).all()

    return check_ratings

def get_average_rating_by_route_id(route_id):
    """Get average of the star ratings by route_id."""

    average_rating = db.session.query(db.func.avg(Rating.stars)).filter(Rating.route_id == route_id).all()

    stars = average_rating[0][0]

    if stars:
        avg_stars = round(stars, 2)
        return avg_stars
    else:
        return "No one has submitted a star rating for this route yet."

def total_rating_by_route_id(route_id):
    """Get total number of star ratings by route_id."""

    total_ratings = db.session.query(db.func.count(Rating.stars)).filter(Rating.route_id == route_id).all()

    rate_times = total_ratings[0][0]

    return rate_times

def get_reviews_by_climber_id(climber_id):
    """Get reviews by climber_id."""

    climber_reviews = db.session.query(Route.route).join(Review).filter(Review.climber_id == climber_id).distinct().all()

    return climber_reviews

def get_ratings_by_climber_id(climber_id):
    """Get ratings by climber_id."""

    climber_ratings = db.session.query(Route.route).join(Rating).filter(Rating.climber_id == climber_id).distinct().all()

    return climber_ratings


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
