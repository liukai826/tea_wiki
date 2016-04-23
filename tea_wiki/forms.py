from wtforms import Form, BooleanField, TextField, PasswordField, validators

class RegisterForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

class LoginForm(Form):
    username = TextField('Username')
    password = PasswordField('Password')
