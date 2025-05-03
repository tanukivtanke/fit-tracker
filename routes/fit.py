from datetime import date, timedelta

from base import app, db
from flask import render_template, request, jsonify
from objects.tables import Dish, Meal, MealGroup, User, Food, MealOrder, DishIngredient

from util import list_to_json, string_to_date, calc_from_food, calc_from_dish, list_to_dict, get_argument, \
    deletion_change_food, calculate_calories_from_day, Nutrients

from auth import *


@app.route('/')
def meals():
    return render_template('fit.html')


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


@app.route('/api/foods')
def get_food():
    return Food.all_json()


@app.route('/api/meals')
def get_all_meals():
    return Meal.all_json()


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
    meals_by_date = sorted(meals_by_date, key=lambda x: MealOrder.find(id=x.meal_order_id).ordering)
    return list_to_json(meals_by_date)


@app.route('/api/get_meals_for_meal_group')
def get_meals_for_meal_group():
    meal_group_id = get_argument('id')
    meals_per_group = Meal.all(meal_group_id=meal_group_id)
    meals_per_group = sorted(meals_per_group, key=lambda x: x.id)
    return list_to_json(meals_per_group)


@app.route('/api/get_meals_for_meal_day_all')
def get_meals_for_meal_day_all():
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

    food_id = received_data['food_id']
    dish_id = received_data['dish_id']
    is_dish = food_id is None
    is_food = dish_id is None
    if is_dish == is_food:
        return 'Cannot add food and dish in the same request', 400

    amount = received_data['amount']
    if amount is None or not isinstance(amount, int):
        return 'Cannot add food or dish without any amount', 400

    if is_food:
        curr_food = Food.find(id=food_id)
        curr_food.last_used = date.today()
        curr_food.update()
        db.session.commit()
    else:
        curr_dish = Dish.find(id=dish_id)
        curr_dish.last_used = date.today()
        curr_dish.update()
        db.session.commit()

    same_meal = Meal.find(meal_group_id=received_data['meal_group_id'],
                          food_id=food_id,
                          dish_id=dish_id)

    if same_meal is None:

        if is_food:
            new_data = calc_from_food(food_id, amount)
        else:
            new_data = calc_from_dish(dish_id, amount)

        new_edible = Meal(meal_group_id=received_data['meal_group_id'],
                          food_id=food_id,
                          dish_id=dish_id,
                          amount=amount,
                          calc_proteins=new_data.proteins,
                          calc_fats=new_data.fats,
                          calc_carbs=new_data.carbs,
                          calc_kcal=new_data.kcal)
        new_edible.save()
        return new_edible.json()

    else:
        new_amount = amount + same_meal.amount
        if new_amount <= 0:
            return same_meal.json()
        if is_food:
            new_data = calc_from_food(food_id, new_amount)
        else:
            new_data = calc_from_dish(dish_id, new_amount)

        same_meal.amount = new_amount
        same_meal.calc_proteins = new_data.proteins
        same_meal.calc_fats = new_data.fats
        same_meal.calc_carbs = new_data.carbs
        same_meal.calc_kcal = new_data.kcal
        same_meal.update()
        return same_meal.json()


@app.route('/api/food/new', methods=['POST'])
def add_food():
    received_data = request.json

    new_food = Food(
        name=received_data['name'],
        proteins=received_data['proteins'],
        fats=received_data['fats'],
        carbs=received_data['carbs'],
        kcal=received_data['kcal'],
        is_deleted=False,
        portion_size=received_data['portion_size'],
        last_used=date.today()
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
        food_to_change.portion_size = received_data['portion_size']
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

    current_ingredient = received_data
    new_ingredient = dish_change(current_ingredient['dish_id_ingredient'],
                                 current_ingredient['dish_id'],
                                 current_ingredient['food_id_ingredient'],
                                 current_ingredient['amount'])

    return jsonify(new_ingredient)


@app.route('/api/dish_ingredient/new_many', methods=['POST'])
def ingredients_edit():
    received_data = request.json

    new_ingredients = []
    for i in range(len(received_data)):
        current_ingredient = received_data[i]
        value = dish_change(current_ingredient['dish_id_ingredient'],
                            current_ingredient['dish_id'],
                            current_ingredient['food_id_ingredient'],
                            current_ingredient['amount'])
        if type(value) == tuple:
            return value
        new_ingredients.append(value)

    return jsonify(new_ingredients)


def dish_change(dish_id_ingr: int, dish_id: int, food_id_ingr: int, amount: float):
    if dish_id_ingr:
        if dish_id == dish_id_ingr:
            return 'Cannot add dish into the same dish', 400

    new_ingredient = DishIngredient(
        food_id_ingredient=food_id_ingr,
        dish_id_ingredient=dish_id_ingr,
        dish_id=dish_id,
        amount=amount,
    )
    new_ingredient.save()
    return new_ingredient.dict()


@app.route('/api/dish_ingredient/delete', methods=['DELETE'])
def del_dish_ingredient():
    received_data = request.json
    id_to_del = received_data['id']
    return jsonify(DishIngredient.delete_by_id(id_to_del))


@app.route('/api/food/delete', methods=['DELETE'])
def del_food():
    received_data = request.json
    food_to_del = deletion_change_food(received_data['id'], True)
    return food_to_del.json()


@app.route('/api/food/revive', methods=['POST'])
def revive_food():
    received_data = request.json
    food_to_rev = deletion_change_food(received_data['id'], False)
    return food_to_rev.json()


@app.route('/api/dish/new', methods=['POST'])
def add_dish():
    received_data = request.json

    new_dish = Dish(
        name=received_data['name'],
        out_of_stock=received_data["out_of_stock"],
        recipe='',
        last_used=date.today(),
        for_dish=received_data["for_dish"]
    )
    new_dish.save()
    return new_dish.json()


@app.route('/api/meal/move', methods=['POST'])
def move_meal():
    received_data = request.json

    res = []
    destination = received_data['move_to_meal_group']
    for i in received_data['meal_ids']:
        meal_to_move = Meal.find(id=i)
        meal_to_move.meal_group_id = destination
        meal_to_move.save()
        res.append(meal_to_move.dict())

    return jsonify(res)


@app.route('/api/meal/duplicate', methods=['POST'])
def duplicate_meal():
    received_data = request.json

    res = []
    destination = received_data['move_to_meal_group']
    for i in received_data['meal_ids']:
        meal_to_copy = Meal.find(id=i)
        new_meal_ing = Meal(
            dish_id=meal_to_copy.dish_id,
            food_id=meal_to_copy.food_id,
            meal_group_id=destination,
            amount=meal_to_copy.amount,
            calc_proteins=meal_to_copy.calc_proteins,
            calc_fats=meal_to_copy.calc_fats,
            calc_carbs=meal_to_copy.calc_carbs,
            calc_kcal=meal_to_copy.calc_kcal,
        )
        new_meal_ing.save()

        res.append(meal_to_copy.dict())

    return jsonify(res)


@app.route('/api/meal/delete_many', methods=['DELETE'])
def del_meal_many():
    received_data = request.json
    res = []
    for i in received_data['meal_ids']:
        res.append(Meal.delete_by_id(i))
    return jsonify(res)


@app.route('/api/get_average')
def calculate_weekly_average():
    user_id = get_argument('user_id')
    view_date = get_argument('date')
    days = int(get_argument('days'))
    view_date = date.fromisoformat(view_date)
    week_start = view_date - timedelta(days=days)

    calories_sum = Nutrients()
    for i in range(days):
        one_day = calculate_calories_from_day(user_id, week_start)
        if one_day.kcal:
            calories_sum += calculate_calories_from_day(user_id, week_start)
        else:
            days -= 1
        week_start += timedelta(days=1)

    if not days:
        return jsonify(Nutrients().dict())

    return jsonify((calories_sum / days).dict())
