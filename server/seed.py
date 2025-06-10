#!/usr/bin/env python3
# server/seed.py

from app import app
from models import db, Pet

with app.app_context():
    # Delete all existing rows in the pets table
    Pet.query.delete()

    # Create a list of Pet instances
    pets = [
        Pet(name="Fido", species="Dog"),
        Pet(name="Whiskers", species="Cat"),
        Pet(name="Hermie", species="Hamster"),
        Pet(name="Slither", species="Snake")
    ]

    # Insert each Pet into the database table
    db.session.add_all(pets)

    # Commit the transaction
    db.session.commit()

    print("🌱 Database successfully seeded with 4 pets!")
