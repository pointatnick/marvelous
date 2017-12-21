from app import db

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140), index=True, unique=True)

    def __repr__(self):
        return "<Character %r>" % (self.name)