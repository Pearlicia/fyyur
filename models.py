from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate
from flask_moment import Moment

app = Flask(__name__)
moment = Moment(app)


app.config.from_object('config')
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:pearlicia@localhost:5432/fyyur'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    city = db.Column(db.String(120), nullable = False)
    state = db.Column(db.String(120), nullable = False)
    address = db.Column(db.String(120), nullable = False)
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # Implement any missing fields, as a database migration using Flask-Migrate
    seeking_description = db.Column(db.String())
    seeking_talent = db.Column(db.Boolean, nullable = False)
    website = db.Column(db.String(120))
    genres = db.Column(db.String(120), nullable = False)
    shows = db.relationship('show', backref ='venues')

class artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    city = db.Column(db.String(120), nullable = False)
    state = db.Column(db.String(120), nullable = False)
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120), nullable = False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # Implement any missing fields, as a database migration using Flask-Migrate
    website = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, nullable = False)
    seeking_description = db.Column(db.String())
    shows = db.relationship('show', backref ='artists')
 
# Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
class show(db.Model):
    __tablename__ = 'show'
    id = db.Column(db.Integer, primary_key = True)
    start_date = db.Column(db.DateTime, nullable = False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id',ondelete="SET NULL",onupdate="cascade"))
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id',ondelete="SET NULL", onupdate="cascade"))
