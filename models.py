from gamelib import db

class Games(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)
    asin = db.Column(db.String(10), nullable=False)
    language = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name