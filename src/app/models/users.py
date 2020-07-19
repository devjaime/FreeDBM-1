from app.models import db

class User(db.Model):
	__tablename__ = 'users'
	
	id = db.Column(db.Integer, primary_key = True, autoincrement=True)
	username = db.Column(db.String(255), nullable = False)
	email =  db.Column(db.String(255), nullable = False)
	password = db.Column(db.String(255), nullable = False)

