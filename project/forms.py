from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms import ValidationError

class LoginForm(FlaskForm):

    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

class RegistrationForm(FlaskForm):

    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), EqualTo("pass_confirm", message="Passwords must match.")])
    pass_confirm = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Username already in use, please try another one.")

class AddContact(FlaskForm):

    name = StringField("Name", validators=[DataRequired()])
    contact_type = StringField("Contact Type", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    mobile_phone = StringField("Mobile Phone", validators=[DataRequired()])
    work_phone = StringField("Work Phone")
    address = StringField("Address")
    company = StringField("Company Name")
    submit = SubmitField("Submit")

