from dataclasses import dataclass

from flask import jsonify
from datetime import datetime

from objects.user import Food, DishIngredient


def list_to_json(obj: list):
    return jsonify([i.dict() for i in obj])


def list_to_dict(obj: list):
    return [i.dict() for i in obj]


def string_to_date(string):
    return datetime.strptime(string, '%Y-%m-%d')


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
        nutri += calc_from_food(i.food_id, i.amount)
        total_amount += i.amount
    total_amount_per_100g = total_amount / 100
    return Nutrients(proteins=nutri.proteins * kg_amount / total_amount_per_100g,
                     fats=nutri.fats * kg_amount / total_amount_per_100g,
                     carbs=nutri.carbs * kg_amount / total_amount_per_100g,
                     kcal=nutri.kcal * kg_amount / total_amount_per_100g)

