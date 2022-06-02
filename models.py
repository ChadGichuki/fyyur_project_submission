from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint
from flask_migrate import Migrate


db = SQLAlchemy()

class Venue(db.Model):
    """Table stores all the venues"""
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    genres = db.Column(db.ARRAY(db.String), nullable=False)
    image_link = db.Column(db.String(500), nullable=True, default='None')
    facebook_link = db.Column(db.String(120), nullable=True, default='None')
    website_link = db.Column(db.String(120), nullable=True, default='None')
    talent_looking = db.Column(db.Boolean, default=False)
    description = db.Column(db.String(), nullable=True)
    upcoming_shows = db.relationship('Show', backref='venue', lazy=True)
   
    def __repr__(self):
      return f'<Venue {self.id}, {self.name}>'

class Artist(db.Model):
    """Table stores all the artists"""
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    genres = db.Column(db.ARRAY(db.String), nullable=False)
    image_link = db.Column(db.String(500), nullable=True, default='None')
    facebook_link = db.Column(db.String(120), nullable=True, default='None')
    website_link = db.Column(db.String(120), nullable=True, default='None')
    venue_looking = db.Column(db.Boolean, default=False)
    description = db.Column(db.String(), nullable=True)
    upcoming_shows = db.relationship('Show', backref='artist', lazy=True)

    def __repr__(self):
        return f'<Venue {self.id}, {self.name}>'

class Show(db.Model):
    """
    Table stores all the shows.

    A show can have only one artist and only one show. 
    However, an artist and a venue can have many shows. 
    (One to many relationships with both)
    """
    __tablename__= 'shows'
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime(timezone=False), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)

    def __repr__(self):
      return f'<Show {self.id}, {self.start_time}'



