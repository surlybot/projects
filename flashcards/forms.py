from wtforms import Form, TextField, TextAreaField, PasswordField, HiddenField, validators, IntegerField

class LoginForm(Form):
    email = TextField("Email", [validators.Required(), validators.Email()])
    password = PasswordField("Password", [validators.Required()])

class NewPostForm(Form):
    title = TextField("title", [validators.Required()])
    body = TextAreaField("body", [validators.Required()])

class NewCollectionForm(Form):
    title = TextField("title", [validators.Required()])
    description = TextAreaField("description", [validators.Required()])

class NewTermForm(Form):
    term = TextField("term", [validators.Required()])
    definition = TextAreaField("definition", [validators.Required()])

class RegisterForm(Form):
    email = TextField("Email", [validators.Required(), validators.Email()])
    first_name = TextField("First Name", [validators.Required()])
    last_name = TextField("Last Name", [validators.Required()])
    password = PasswordField("Password", [validators.Required()])
