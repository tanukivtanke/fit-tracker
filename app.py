import auth
from base import app, db
from flask import render_template, request, jsonify
from objects.user import Dish, Meal, MealGroup, User, Food, MealOrder
from datetime import date

from util import list_to_json, string_to_date


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


@app.route('/api/meal_orders')
def get_all_meal_orders():
    return MealOrder.all_json()


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


@app.route('/api/meal_groups/new', methods=['POST'])
def add_new_meal():
    received_data = request.json
    new_meal = MealGroup(user_id=received_data['user_id'],
                         meal_name=received_data['meal_name'],
                         day=string_to_date(received_data['day']),
                         meal_order_id=received_data['meal_order_id'])
    new_meal.save()
    return new_meal.json()


@app.route('/api/meal/delete', methods=['DELETE'])
def del_meal():
    received_data = request.json
    id_to_del = received_data['id']
    return jsonify(Meal.delete_by_id(id_to_del))


@app.route('/api/meal/new', methods=['POST'])
def add_meal():
    received_data = request.json

    food_id_none = received_data['food_id'] is None
    dish_id_none = received_data['dish_id'] is None
    if food_id_none == dish_id_none:
        return 'Cannot add food and dish in the same request', 400

    amount = received_data['amount']
    if amount is None or not isinstance(amount, int) or amount <= 0:
        return 'Cannot add food or dish without any amount or negative amount', 400

    new_edible = Meal(meal_group_id=received_data['meal_group_id'],
                      food_id=received_data['food_id'],
                      dish_id=received_data['dish_id'],
                      amount=received_data['amount'])
    new_edible.save()
    return new_edible.json()


@app.route('/user/<username>')
def show_user_profile(username):
    return render_template('meals.html', name=username)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, use_reloader=False)
