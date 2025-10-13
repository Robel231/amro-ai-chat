from . import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    user = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<Message {self.id}>'
