from app import db, pwd_context
from app.associations import participation

class User(db.Model):

	__tablename__ = 'users'

	id = db.Column(db.Integer(), primary_key=True, index=True)
	username = db.Column(db.String(128), nullable=False, unique=True)
	email = db.Column(db.String(128), unique=True, nullable=False)
	password_hash = db.Column(db.String(128), nullable=False)

	activities = db.relationship("Activity", secondary=participation)
	# achievements = db.relationship("Achievement", secondary="achievement_link")

	@property
	def password(self):
		"""
		Prevent pasword_hash from being accessed
		"""
		raise AttributeError('password is not a readable attribute.')

	@password.setter
	def password(self, password):
		"""
		Set password to a hashed password
		"""

		self.password_hash = pwd_context.encrypt(password)

	def verify_password(self, password):
		"""
		Check if hashed password matches actual password
		"""
		return pwd_context.verify(password, self.password_hash)

	def __repr__(self):
		return f'<User: {self.username}>'