from app import db
from app.associations import participation
from .interface import ActivityInterface

class Activity(db.Model):
	__tablename__ = 'activities'

	id = db.Column(db.Integer(), primary_key=True)

	name = db.Column(db.String(128), nullable=False)
	description = db.Column(db.String(512))

	activity_time = db.Column(db.DateTime(), nullable=False)
	location = db.Column(db.String(256), nullable=False)

	is_public = db.Column(db.Boolean(), default=True)

	# creator = db.Column(
	# 	db.String(128), db.ForeignKey('users.id', ondelete='CASCADE'),
	# 	nullable=False
	# )

	# category = db.Column(
	# 	db.String(128), db.ForeignKey('categories.id')
	# )
	#
	# participants = db.relationship("User", secondary=participation)

	def update(self, changes: ActivityInterface):
		for key, val in changes.items():
			setattr(self, key, val)
		return self

	def __repr__(self):
		return f'<Activity {self.id}>'
		# return f'<Activity {self.id} - created by {self.creator.username}>'
