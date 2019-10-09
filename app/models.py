from app import db
from app import app


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    clientname = db.Column(db.String(120), index=True)

    def __repr__(self):
        return '<Client {}>'.format(self.clientname)
