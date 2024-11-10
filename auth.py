from flask_httpauth import HTTPBasicAuth

from flask import request, Response, after_this_request
from secrets import token_hex

from base import app


auth = HTTPBasicAuth()

users = {
    "admin": open('password').read().strip()
}


# List to store valid session keys
valid_sessions = []

def check_auth(username, password):
    """Check if a username/password combination is valid."""
    return username in users and users[username] == password

def authenticate():
    """Send a 401 response to trigger HTTP Basic Auth."""
    return Response(
        'Authentication required.', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})

@app.before_request
def check_session_and_authenticate():
    session_key = request.cookies.get('SESSION')
    if session_key in valid_sessions:
        # Session is valid; proceed with the request
        return
    else:
        # Session is invalid; require authentication
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        else:
            # Credentials are valid; generate a new session key
            session_key = token_hex(32)  # Generates a 64-character hex string
            valid_sessions.append(session_key)
            @after_this_request
            def set_session_cookie(response):
                # Set the session cookie to last for 3 years
                response.set_cookie('SESSION', session_key, max_age=3*365*24*60*60)
                return response
