from app import db
from datetime import datetime, UTC


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    service = db.Column(db.String(100), nullable=True)
    date = db.Column(db.Date, default=datetime.now(UTC).date, nullable=False)
    time = db.Column(db.Time, default=datetime.now(UTC).time, nullable=False)
