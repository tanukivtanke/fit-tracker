from dataclasses import dataclass

from flask import jsonify, request
from datetime import datetime, date, timedelta

from objects.tables import Food, DishIngredient, MealGroup, Meal


def list_to_json(obj: list):
    return jsonify([i.dict() for i in obj])


def list_to_dict(obj: list):
    return [i.dict() for i in obj]


def string_to_date(string):
    return datetime.strptime(string, '%Y-%m-%d')


def get_argument(arg_name):
    return request.args.get(arg_name, default="", type=str)


@dataclass
class Nutrients:
    proteins: float = 0
    fats: float = 0
    carbs: float = 0
    kcal: float = 0

    def __add__(self, other):
        return Nutrients(self.proteins + other.proteins,
                         self.fats + other.fats,
                         self.carbs + other.carbs,
                         self.kcal + other.kcal)

    def __iadd__(self, other):
        self.proteins += other.proteins
        self.fats += other.fats
        self.carbs += other.carbs
        self.kcal += other.kcal
        return self

    def __truediv__(self, integer):
        return Nutrients(self.proteins / integer,
                         self.fats / integer,
                         self.carbs / integer,
                         self.kcal / integer)

    def dict(self):
        return obj_to_dict(self)


def obj_to_dict(obj):
    return {k: v for k, v in obj.__dict__.items() if not k.startswith("_")}


def calc_from_food(food_id, amount) -> Nutrients:
    kg_amount = amount / 100
    food: Food = Food.find(id=food_id)
    nutrients = Nutrients(proteins=food.proteins * kg_amount,
                          fats=food.fats * kg_amount,
                          carbs=food.carbs * kg_amount,
                          kcal=food.kcal * kg_amount)
    return nutrients


def calc_from_dish(dish_id, amount) -> Nutrients:
    kg_amount = amount / 100
    ingredients = DishIngredient.all(dish_id=dish_id)
    nutri = Nutrients()
    if len(ingredients) == 0:
        return nutri
    total_amount = 0
    for i in ingredients:
        if i.food_id_ingredient:
            nutri += calc_from_food(i.food_id_ingredient, i.amount)
            total_amount += i.amount
        elif i.dish_id_ingredient:
            nutri += calc_from_dish(i.dish_id_ingredient, i.amount)
            total_amount += i.amount
    total_amount_per_100g = total_amount / 100
    return Nutrients(proteins=nutri.proteins * kg_amount / total_amount_per_100g,
                     fats=nutri.fats * kg_amount / total_amount_per_100g,
                     carbs=nutri.carbs * kg_amount / total_amount_per_100g,
                     kcal=nutri.kcal * kg_amount / total_amount_per_100g)


def deletion_change_food(food_id, is_deleted):
    id_to_del = food_id
    food_to_del = Food.find(id=id_to_del)
    food_to_del.is_deleted = is_deleted
    food_to_del.update()
    return food_to_del


def calculate_calories_from_day(user_id, day):
    meals = MealGroup.all(user_id=user_id, day=day)
    nutrients_to_sum = Nutrients()
    for meal in meals:
        this_meal = Meal.all(meal_group_id=meal.id)
        for component in this_meal:
            nutrient = Nutrients(component.calc_proteins, component.calc_fats, component.calc_carbs, component.calc_kcal)
            nutrients_to_sum += nutrient
    return nutrients_to_sum

