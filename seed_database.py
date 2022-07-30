"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb climbs")
os.system("createdb climbs")

model.connect_to_db(server.app)
model.db.create_all()

# load climbing route data from JSON file
with open('data/climbs.json') as f:
    climbs_data = json.loads(f.read())

# create routes, store them in list so we can use them
# to create fake ratings later?

routes_in_db = []
for climb in climbs_data:
    route, grade, latitude, longitude, picture_path = (
        climb["route"],
        climb["grade"],
        climb["latitude"],
        climb["longitude"],
        climb["picture_path"],
    )
    db_climb = crud.create_route(route, grade, latitude, longitude, picture_path)
    routes_in_db.append(db_climb)

model.db.session.add_all(routes_in_db)
model.db.session.commit()


