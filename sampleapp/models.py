from . import db

class Questions(db.Model):
    __tablename__ = 'questions'

    keyid = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String(25))
    question = db.Column(db.String(150))
    uresponse = db.Column(db.String(10))
    unotes = db.Column(db.String(150))
    uasset = db.Column(db.String(150))

    



