from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField
from wtforms.validators import Required


class ModEntry(Form):
    title = TextField("Title", [Required()])
    description = TextAreaField("Description", [Required()])
    tags = TextField("Tags", [Required()])
    submit = SubmitField("Save")
