from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User

class RegistrationForm(FlaskForm):
  username = StringField('Nazwa użytkownika', validators=[DataRequired(), Length(min=2, max=20)])
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Hasło', validators=[DataRequired()])
  confirm_password = PasswordField('Potwierdź hasło', validators=[DataRequired(), EqualTo('password')])

  submit = SubmitField('Zarejestruj się')

  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user:
      raise ValidationError('Ten użytkownik już istnieje! Wybież inną nazwę użytkownika!')
  
  def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user:
      raise ValidationError('Ten adres email już istnieje! Wybież inny!')

class LoginForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Hasło', validators=[DataRequired()])
  remember = BooleanField('Zapamiętaj mnie')
  
  submit = SubmitField('Zaloguj')


class UpdateAccountForm(FlaskForm):
  username = StringField('Nazwa użytkownika', validators=[DataRequired(), Length(min=2, max=20)])
  email = StringField('Email', validators=[DataRequired(), Email()])
  picture = FileField('Zmień zdjęcie profilowe', validators=[FileAllowed(['jpg', 'png'])])

  submit = SubmitField('Zapisz zmiany')

  def validate_username(self, username):
    if username.data != current_user.username:
      user = User.query.filter_by(username=username.data).first()
      if user:
        raise ValidationError('Ten użytkownik już istnieje! Wybież inną nazwę użytkownika!')
  
  def validate_email(self, email):
    if email.data != current_user.email:
      user = User.query.filter_by(email=email.data).first()
      if user:
        raise ValidationError('Ten adres email już istnieje! Wybież inny!')


class RequestResetForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired(), Email()])
  submit = SubmitField('Reset hasła')

  def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if not user:
      raise ValidationError('Nie ma konta skojarzonego z tym adresem email!')


class ResetPasswordForm(FlaskForm):
  password = PasswordField('Hasło', validators=[DataRequired()])
  confirm_password = PasswordField('Potwierdź hasło', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Resetuj hasło')
