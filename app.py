import auth
from base import app, db
from flask import render_template, request
from objects.user import Dish, Meal, MealGroup, User, Food, MealOrder
from datetime import date


@app.route('/')
def hello_world():
    return render_template('hello.html', name='qwe')


@app.route('/about')
def about():
    return 'This is the about page'


@app.route('/api/users')
def get_users():
    return User.all_json()


@app.route('/api/foods')
def get_food():
    return Food.all_json()


@app.route('/api/meals')
def get_meals():
    return Meal.all_json()


def get_argument(arg_name):
    return request.args.get(arg_name, default="", type=str)


@app.route('/api/meal_groups')
def get_meal_groups():
    return MealGroup.all_json()


@app.route('/api/dishes')
def get_dishes():
    return Dish.all_json()


@app.route('/api/today_meals')
def get_today_meals():
    username = get_argument('user')
    user_id = User.find(username=username).id
    today = date.today()
    today_meals = MealGroup.all(user_id=user_id, day=today)
    return sorted(today_meals, key=lambda x:  MealOrder.find(id=x.meal_order_id).ordering)


@app.route('/user/<username>')
def show_user_profile(username):
    return render_template('hello.html', name=username)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, use_reloader=False)
