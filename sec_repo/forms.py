from flask_wtf import Form, TextField, TextAreaField, SubmitField


class AddEntry(Form):
    title = TextField("Title")
    description = TextAreaField("Description")
    tags = TextField("Tags")
    submit = SubmitField("Save")
