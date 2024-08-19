from base import app, db
from flask import render_template, request, jsonify
from objects.user import Dish, Meal, MealGroup, User, Food, MealOrder, DishIngredient

from util import list_to_json, string_to_date, calc_from_food, calc_from_dish, list_to_dict

from auth import *

from sys import argv

@app.route('/')
def hello_world():
    return render_template('meals.html')


@app.route('/about')
def about():
    return 'This is the about page'


@app.route('/api/all_static')
def get_all_static():
    return jsonify({
        "users": User.all_dict(),
        "meal_orders": MealOrder.all_dict(),
        "foods": Food.all_dict(),
        "dishes": Dish.all_dict(),
        "dish_ingredients": DishIngredient.all_dict()
    })


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


@app.route('/api/dish_ingredients')
def get_dish_ingredients():
    return DishIngredient.all_json()


@app.route('/api/meal_orders')
def get_all_meal_orders():
    return MealOrder.all_json()


@app.route('/api/get_meals_for_day')
def get_meals_for_day():
    user_id = get_argument('user_id')
    meal_date = get_argument('date')
    meals_by_date = MealGroup.all(user_id=user_id, day=meal_date)
    meals_by_date = sorted(meals_by_date, key=lambda x:  MealOrder.find(id=x.meal_order_id).ordering)
    return list_to_json(meals_by_date)


@app.route('/api/get_meals_for_meal_group')
def get_meals_for_meal_group():
    meal_group_id = get_argument('id')
    meals_per_group = Meal.all(meal_group_id=meal_group_id)
    meals_per_group = sorted(meals_per_group, key=lambda x:  x.id)
    return list_to_json(meals_per_group)


@app.route('/api/get_meals_for_meal_group_all')
def get_meals_for_meal_group_all():
    user_id = get_argument('user_id')
    meal_date = get_argument('date')
    meals_by_date = MealGroup.all(user_id=user_id, day=meal_date)
    meals_by_date = sorted(meals_by_date, key=lambda x: MealOrder.find(id=x.meal_order_id).ordering)
    meals_ids = [i.id for i in meals_by_date]
    meal_to_group = {}
    for i in meals_ids:
        meal_group_id = i
        meals_per_group = Meal.all(meal_group_id=meal_group_id)
        meals_per_group = sorted(meals_per_group, key=lambda x: x.id)
        meal_to_group[str(i)] = list_to_dict(meals_per_group)
    return jsonify({
        'meal_groups': list_to_dict(meals_by_date),
        'meals_for_meal_group': meal_to_group
    })


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


@app.route('/api/meal_group/delete', methods=['DELETE'])
def del_meal_group():
    received_data = request.json
    id_to_del = received_data['id']
    return jsonify(MealGroup.delete_by_id(id_to_del))


@app.route('/api/meal/new', methods=['POST'])
def add_meal():
    received_data = request.json

    is_dish = received_data['food_id'] is None
    is_food = received_data['dish_id'] is None
    if is_dish == is_food:
        return 'Cannot add food and dish in the same request', 400

    amount = received_data['amount']
    if amount is None or not isinstance(amount, int) or amount <= 0:
        return 'Cannot add food or dish without any amount or negative amount', 400

    if is_food:
        new_data = calc_from_food(received_data['food_id'], received_data['amount'])
    else:
        new_data = calc_from_dish(received_data['dish_id'], received_data['amount'])

    new_edible = Meal(meal_group_id=received_data['meal_group_id'],
                      food_id=received_data['food_id'],
                      dish_id=received_data['dish_id'],
                      amount=received_data['amount'],
                      calc_proteins=new_data.proteins,
                      calc_fats=new_data.fats,
                      calc_carbs=new_data.carbs,
                      calc_kcal=new_data.kcal)
    new_edible.save()
    return new_edible.json()


@app.route('/api/food/new', methods=['POST'])
def add_food():
    received_data = request.json

    new_food = Food(
        name=received_data['name'],
        proteins=received_data['proteins'],
        fats=received_data['fats'],
        carbs=received_data['carbs'],
        kcal=received_data['kcal']
    )
    new_food.save()
    return new_food.json()


@app.route('/api/food/edit', methods=['POST'])
def edit_food():
    received_data = request.json

    food_to_change = Food.find(id=received_data['id'])
    if food_to_change is not None:
        food_to_change.name = received_data['name']
        food_to_change.proteins = received_data['proteins']
        food_to_change.fats = received_data['fats']
        food_to_change.carbs = received_data['carbs']
        food_to_change.kcal = received_data['kcal']
        food_to_change.update()
        return food_to_change.json()
    else:
        return ''


@app.route('/api/dish/edit', methods=['POST'])
def edit_dish():
    received_data = request.json

    dish_to_change = Dish.find(id=received_data['id'])
    if dish_to_change is not None:
        dish_to_change.name = received_data['name']
        dish_to_change.out_of_stock = received_data['out_of_stock']
        dish_to_change.update()
        return dish_to_change.json()
    else:
        return ''


@app.route('/api/dish_recipe/edit', methods=['POST'])
def edit_recipe():
    received_data = request.json

    dish_to_change = Dish.find(id=received_data['id'])
    if dish_to_change is not None:
        dish_to_change.recipe = received_data['recipe']
        dish_to_change.update()
        return dish_to_change.json()
    else:
        return ''


@app.route('/api/dish_ingredient/new', methods=['POST'])
def ingredient_edit():
    received_data = request.json

    new_ingredient = DishIngredient(
        food_id=received_data['food_id'],
        dish_id=received_data['dish_id'],
        amount=received_data['amount'],
    )
    new_ingredient.save()
    return new_ingredient.json()


@app.route('/api/dish_ingredient/delete', methods=['DELETE'])
def del_dish_ingredient():
    received_data = request.json
    id_to_del = received_data['id']
    return jsonify(DishIngredient.delete_by_id(id_to_del))


@app.route('/api/dish/new', methods=['POST'])
def add_dish():
    received_data = request.json

    new_dish = Dish(
        name=received_data['name'],
        out_of_stock=False,
        recipe=''
    )
    new_dish.save()
    return new_dish.json()


@app.route('/user/<username>')
def show_user_profile(username):
    return render_template('meals.html', name=username)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    if 'prod' in argv:
        app.run(host='0.0.0.0', port=80)
    else:
        app.run(debug=True, use_reloader=False)
