from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired("Please enter your name.")])
    email = StringField('E-mail', validators=[InputRequired(), Email()])
    subject = StringField('Subject', validators=[InputRequired()])
    message = TextAreaField('Message', validators=[InputRequired()], render_kw={"rows": 5, "cols": 42})


    