
# Within the database model - it contains an id, username, and email column
# Therefore, the model has access to id, username, and email databases
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # added columns for user data model
    money = db.Column(db.Float, unique=False, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
