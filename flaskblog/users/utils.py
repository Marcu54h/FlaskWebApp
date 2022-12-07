import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail

def save_picture(form_picture):
  random_hex = secrets.token_hex(12)
  _, f_ext = os.path.splitext(form_picture.filename)
  picture_fn = random_hex + f_ext
  picture_path = os.path.join(current_app.root_path, 'static', 'profile_pics', picture_fn)
  form_picture.save(picture_path)
  output_size = (125, 125)
  img = Image.open(picture_path)
  img.thumbnail(output_size) 
  img.save(picture_path)

  return picture_fn


def send_reset_email(user):
  token = user.get_reset_token()
  msg = Message('Żądanie zresetowania hasła', sender="adam.marzec@gmail.com", recipients=[user.email])
  msg.body = f'''W celu zresetowania hasła odwiedź następujący odnośnik:
{url_for('users.reset_token', token=token, _external=True)}

Jeżeli nie żądałeś resetowania hasła po prostu zignoruj ten email.
'''
  mail.send(msg)

