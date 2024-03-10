from flask_httpauth import HTTPBasicAuth

from base import app


auth = HTTPBasicAuth()


@app.before_request
@auth.login_required
def before_request():
    pass


users = {
    "admin": open('password').read().strip()
}


@auth.verify_password
def verify_password(username, password):
    if username in users and users.get(username) == password:
        return username
