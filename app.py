import auth
from base import app, db
from flask import render_template, request, jsonify
from objects.user import Dish, Meal, MealGroup, User, Food, MealOrder
from datetime import date

from util import list_to_json


@app.route('/')
def hello_world():
    return render_template('meals.html')


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
def get_all_meals():
    return Meal.all_json()


def get_argument(arg_name):
    return request.args.get(arg_name, default="", type=str)


@app.route('/api/meal_groups')
def get_meal_groups():
    return MealGroup.all_json()


@app.route('/api/dishes')
def get_dishes():
    return Dish.all_json()


@app.route('/api/get_meals_for_day')
def get_meals_for_day():
    username = get_argument('user')
    meal_date = get_argument('date')
    user_id = User.find(username=username).id
    meals_by_date = MealGroup.all(user_id=user_id, day=meal_date)
    meals_by_date = sorted(meals_by_date, key=lambda x:  MealOrder.find(id=x.meal_order_id).ordering)
    return list_to_json(meals_by_date)


@app.route('/api/get_meals_for_meal_group')
def get_meals_for_meal_group():
    meal_group_id = get_argument('id')
    meals_per_group = Meal.all(meal_group_id=meal_group_id)
    meals_per_group = sorted(meals_per_group, key=lambda x:  x.id)
    return list_to_json(meals_per_group)


@app.route('/user/<username>')
def show_user_profile(username):
    return render_template('meals.html', name=username)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, use_reloader=False)
