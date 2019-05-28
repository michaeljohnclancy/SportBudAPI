from app import db

class Activity(db.Model):
	__tablename__ = 'activities'

	id = db.Column(db.Integer(), primary_key=True)

	name = db.Column(db.String(128), required=True)
	description = db.Column(db.String(512))

	event_time = db.Column(db.Datetime(), required=True)
	event_location = db.Column(db.String(256), required=True)

	is_public = db.Column(db.Boolean(), default=True)

	creator = db.Column(
		db.String(128), db.ForeignKey('users.id', ondelete='CASCADE')
	)

	# category = db.Column(
	# 	db.String(128), db.ForeignKey('categories.id')
	# )
	#
	participants = db.relationship("User", secondary="participation", viewonly=True)

	def __repr__(self):
		return f'<Activity {self.id} - created by {self.creator.username}>'
