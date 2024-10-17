from enum import unique
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class patient(db.Model, UserMixin):
    __tablename__ = 'patient'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    phone_number = db.Column(db.String(13), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return '<patient %r>' % self.username


class hospital(db.Model, UserMixin):
    __tablename__ = 'hospital'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    address = db.Column(db.String(255), unique=False, nullable=False)
    phone_number = db.Column(db.String(13), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    bloods = db.relationship('Blood', backref='hospital', lazy=True)

    def __repr__(self):
        return '<Hospital %r>' % self.email


class event_organizer(db.Model, UserMixin):
    __tablename__ = 'event_organizer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    phone_number = db.Column(db.String(13), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return '<event_organizer %r>' % self.username


class Blood(db.Model, UserMixin):
    __tablename__ = 'blood'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(3), nullable=False)
    hospital_id = db.Column(db.Integer, db.ForeignKey('hospital.id'), nullable=False)

    # Hubungan satu ke satu dengan blood_stock
    blood_stock = db.relationship('BloodStock', backref='blood', uselist=False)

    def __repr__(self):
        return '<Blood %r>' % self.type


class BloodStock(db.Model, UserMixin):
    __tablename__ = 'blood_stock'

    id = db.Column(db.Integer, primary_key=True)
    stock = db.Column(db.Integer, nullable=False)

    # Foreign key untuk hubungan satu ke satu dengan blood
    blood_id = db.Column(db.Integer, db.ForeignKey('blood.id'), nullable=False)

    def __repr__(self):
        return '<BloodStock %r>' % self.stockw

class event(db.Model):
    __tablename__='event'

    id= db.Column(db.Integer, primary_key=True)
    eventName= db.Column(db.String(200), nullable=False , unique=False)
    location = db.Column(db.String(200), nullable=False, unique = False)
    organizerName=db.Column(db.String(200), nullable=False, unique=False)
    description = db.Column(db.String(400), nullable=False, unique=False)


    def __repr__(self):
        return '<Event: %r' %self.eventName
        