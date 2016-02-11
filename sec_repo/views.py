from flask import render_template, flash, request, redirect, url_for

from sec_repo import app, db
from models import Entry
from forms import AddEntry

from logging import INFO
app.logger.setLevel(INFO)



bookmarks = []


def store_bookmarks(title, description, tags):
    bookmarks.append(dict(
        title=title,
        description=description,
        tags=tags
    ))


@app.route('/')
@app.route('/index')
def index():
    en_tags = Entry.all_tags()
    en = Entry.all_en()
    tags = []
    tags.extend(["".join(x) for x in en_tags])
    unique_tags = []
    for _index in tags:
        unique_tags.extend(_index.split(";"))
    return render_template('index.html', tag_entries=set(unique_tags), entries=en)


@app.route('/add', methods=["GET", "POST"])
def add():
    form = AddEntry()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        tags = form.tags.data
        en = Entry(title=title, description=description, tags=tags)
        db.session.add(en)
        db.session.commit()
        flash("The entry was saved to the database")
        app.logger.debug('stored entry: ' + title + "\n" + description + "\n" + tags)

    return render_template('add.html', form=form)


@app.route('/search', methods=["GET", "POST"])
def search():

    query = request.args.get("query")
    app.logger.debug('the value or query is:' +str(query))
    if query:
        results = Entry.search_tags(query)
    else:
        query = ''
        results = Entry.query.limit(5)
    return render_template('search.html', query=query, results=results)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

