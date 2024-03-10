import auth
from base import app, db
from flask import render_template, jsonify
from objects.user import User


@app.route('/')
def hello_world():
    return 'Hello, World! 123'


@app.route('/about')
def about():
    return 'This is the about page'


@app.route('/users')
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username} for user in users])


@app.route('/user/<username>')
def show_user_profile(username):
    return render_template('hello.html', name=username)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
