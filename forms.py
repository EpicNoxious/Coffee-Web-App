from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email
from wtforms import StringField, SubmitField, PasswordField


class SignUp(FlaskForm):
    name = StringField("Name", validators=[DataRequired()], render_kw={"placeholder": "Your Name"})
    email = StringField("Email", validators=[DataRequired(), Email()], render_kw={"placeholder": "Your Email"})
    password = PasswordField("Password", validators=[DataRequired()], render_kw={"placeholder": "Your Password"})
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired()], render_kw={"placeholder": "Confirm Password"})
    signup = SubmitField("Sign Up")
class SignIn(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()], render_kw={"placeholder": "Your Email"})
    password = PasswordField("Password", validators=[DataRequired()], render_kw={"placeholder": "Your Password"})
    signin = SubmitField("Sign In")

class Menu(FlaskForm):
    add_es = SubmitField("+ Espresso")
    remove_es = SubmitField("- Espresso")
    add_la = SubmitField("+ Latte")
    remove_la = SubmitField("- Latte")
    add_ca = SubmitField("+ Cappuccino")
    remove_ca = SubmitField("- Cappuccino")
    add_cb = SubmitField("+ Brew")
    remove_cb = SubmitField("- Brew")
    add_am = SubmitField("+ Americano")
    remove_am = SubmitField("- Americano")
    add_ma = SubmitField("+ Macchiato")
    remove_ma = SubmitField("- Macchiato")
    add_fw = SubmitField("+ FlatWhite")
    remove_fw = SubmitField("- FlatWhite")
    add_af = SubmitField("+ Affogato")
    remove_af = SubmitField("- Affogato")
    add_te = SubmitField("+ Tea")
    remove_te = SubmitField("- Tea")
    add_cm = SubmitField("+ Shake")
    remove_cm = SubmitField("- Shake")
    add_cr = SubmitField("+ Breve")
    remove_cr = SubmitField("- Breve")
    add_mo = SubmitField("+ Mocha")
    remove_mo = SubmitField("- Mocha")


class Buy(FlaskForm):
    submit = SubmitField("Buy Me")

#
# class Navigation(FlaskForm):
#     home = SubmitField("Home")
#     register = SubmitField("Register")
#     menu = SubmitField("Menu")
#     about = SubmitField("About")
#     signout = SubmitField("Sign Out")