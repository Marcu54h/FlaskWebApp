import os

class Config:
  DEBUG = True
  SECRET_KEY = 'e2009b2879b34811ff6b677babf4ad420ab9c0d5f2ed84b9'
  SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
  SERVER_NAME = "localhost:5000"
  MAIL_SERVER = 'smtp.gmail.com'
  MAIL_PORT = 465
  MAIL_USE_SSL = True
  MAIL_USERNAME = os.environ.get('EMAIL_USERNAME')
  MAIL_PASSWORD = os.environ.get('EMAIL_PASS')