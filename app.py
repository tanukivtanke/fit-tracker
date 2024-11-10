from sys import argv
from routes.fit import *
from routes.gym import *


@app.route('/api/users')
def get_users():
    return User.all_json()


@app.route('/user/<username>')
def show_user_profile(username):
    return render_template('fit.html', name=username)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    if 'prod' in argv:
        app.run(host='0.0.0.0', port=80)
    else:
        app.run(debug=True, use_reloader=False)
