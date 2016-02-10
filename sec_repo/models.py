from sec_repo import db


class Entry(db.Model):
	__tablename__ = 'entries'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.Text, nullable=False)
	description = db.Column(db.String(), nullable=False)
	tags = db.Column(db.Text, nullable=False)

	@staticmethod
	def newest(num):
		return Entry.query.order_by(desc(Entry.id)).limit(num)

	@staticmethod
	def all_tags():
		return Entry.query.with_entities(Entry.tags).all()

	@staticmethod
	def search_tags(search_term):
		return Entry.query.filter(Entry.tags.like('%' + search_term + '%')).all()

	@staticmethod
	def all_en():
		return Entry.query.all()

	def __repr__(self):
		return "<Entry with title: '{}'\n and description '{}'\n and tags: '{}'>".format(self.title, self.description, self.tags)