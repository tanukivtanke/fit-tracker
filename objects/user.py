from base import db
from objects.abstract_object import AbstractObject


class User(AbstractObject):
    __tablename__ = 'user'

    username = db.Column(db.String(80), unique=True, nullable=False)
    image = db.Column(db.String(255))


class Food(AbstractObject):
    __tablename__ = 'food'

    name = db.Column(db.String, unique=True, nullable=False)
    proteins = db.Column(db.Float, nullable=False)
    fats = db.Column(db.Float, nullable=False)
    carbs = db.Column(db.Float, nullable=False)
    kcal = db.Column(db.Float, nullable=False)


class Dish(AbstractObject):
    __tablename__ = 'dish'

    name = db.Column(db.String, unique=True, nullable=False)
    out_of_stock = db.Column(db.Boolean, nullable=False)
    recipe = db.Column(db.String, nullable=False)


class DishIngredient(AbstractObject):
    __tablename__ = 'dish_ingredient'

    dish_id = db.Column(db.Integer, nullable=False)
    food_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)


class Meal(AbstractObject):
    __tablename__ = 'meal'

    dish_id = db.Column(db.Integer)
    food_id = db.Column(db.Integer)
    amount = db.Column(db.Integer, nullable=False)
    meal_group_id = db.Column(db.Integer, nullable=False)
    calc_proteins = db.Column(db.Float, nullable=False)
    calc_fats = db.Column(db.Float, nullable=False)
    calc_carbs = db.Column(db.Float, nullable=False)
    calc_kcal = db.Column(db.Float, nullable=False)


class MealGroup(AbstractObject):
    __tablename__ = 'meal_group'

    user_id = db.Column(db.Integer, nullable=False)
    day = db.Column(db.Date, nullable=False)
    meal_order_id = db.Column(db.Integer, nullable=False)
    meal_name = db.Column(db.String)


class MealOrder(AbstractObject):
    __tablename__ = 'meal_order'

    name = db.Column(db.String, unique=True, nullable=False)
    ordering = db.Column(db.Integer, nullable=False)



