from sec_repo import app, db
from sec_repo.models import Entry
from flask.ext.script import Manager, prompt_bool

manager = Manager(app)


@manager.command
def dropdb():
    if promt_bool("Are you sure you want to lose all your data"):
        db.drop_all()
        print 'Dropped the database'


@manager.command
def initdb():
    db.create_all()
    print 'Initialized the database'

if __name__ == '__main__':
    manager.run()
