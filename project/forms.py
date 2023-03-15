from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms import ValidationError

# LOGIN FORM
class LoginForm(FlaskForm):

    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")


# REGISTRATION FORM
class RegistrationForm(FlaskForm):

    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), EqualTo("pass_confirm", message="Passwords must match.")])
    pass_confirm = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Username already in use, please try another one.")


# ADD CONTACT FORM
class AddContact(FlaskForm):

    name = StringField("Name", validators=[DataRequired()])
    contact_type = StringField("Contact Type", validators=[DataRequired()])
    email = StringField("Email")
    mobile_phone = StringField("Mobile Phone")
    work_phone = StringField("Work Phone")
    address = StringField("Address")
    company = StringField("Company Name")
    submit = SubmitField("Submit")

# ADD note FORM
class AddNote(FlaskForm):

    note = TextAreaField("Note", validators=[DataRequired()])
    submit = SubmitField("Submit")

# FUNCTION USED ON EDIT note ROUTE, IT WILL USE ADDNOTE FORM ABOVE AND CURRENT CONTENT OF note AS DEFAULT VALUE FOR TEXT AREA DISPLAYED
def get_note_form(notes):
    class EditNote(AddNote):
        note = TextAreaField("Note", validators=[DataRequired()], default=notes)
    return EditNote()

class SearchForm(FlaskForm):

    searched = StringField("Search", validators=[DataRequired()])
    submit = SubmitField("Submit")