"""Model for climbing routes review app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Climber(db.Model):
    """A climber."""

    __tablename__ = 'climbers'

    climber_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    goals = db.Column(db.Text)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __repr__(self):
        return f"<Climber climber_id={self.climber_id} email={self.email}>"


class Route(db.Model):
    """A climbing route."""

    __tablename__ = 'routes'

    route_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    route = db.Column(db.String)
    grade = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    picture_path = db.Column(db.String)

    def __repr__(self):
        return f"<Route route_id={self.route_id} route={self.route}>"


class Review(db.Model):
    """A review of a climbing route."""

    __tablename__ = 'reviews'

    review_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    route_id = db.Column(db.Integer, db.ForeignKey("routes.route_id"))
    climber_id = db.Column(db.Integer, db.ForeignKey("climbers.climber_id"))
    date = db.Column(db.Date)
    content = db.Column(db.Text)

    route = db.relationship("Route", backref="reviews")
    climber = db.relationship("Climber", backref="reviews")

    def __repr__(self):
        return f"<Review review_id={self.review_id} content={self.content}>"


class Rating(db.Model):
    """A rating of how fun a climbing route is."""

    __tablename__ = 'ratings'

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    route_id = db.Column(db.Integer, db.ForeignKey("routes.route_id"))
    climber_id = db.Column(db.Integer, db.ForeignKey("climbers.climber_id"))
    stars = db.Column(db.Integer)

    route = db.relationship("Route", backref="ratings")
    climber = db.relationship("Climber", backref="ratings")

    def __repr__(self):
        return f"<Rating rating_id={self.rating_id} stars={self.stars}>"


def connect_to_db(flask_app, db_uri="postgresql:///climbs", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == "__main__":
    from server import app

    connect_to_db(app)