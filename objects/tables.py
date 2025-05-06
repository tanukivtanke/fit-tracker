from base import db
from objects.abstract_object import AbstractObject


class User(AbstractObject):
    __tablename__ = 'user'

    username = db.Column(db.String(80), unique=True, nullable=False)
    image = db.Column(db.String(255))
    color = db.Column(db.String(255))
    image_gym = db.Column(db.String(255))


class Food(AbstractObject):
    __tablename__ = 'fit_food'

    name = db.Column(db.String, unique=True, nullable=False)
    proteins = db.Column(db.Float, nullable=False)
    fats = db.Column(db.Float, nullable=False)
    carbs = db.Column(db.Float, nullable=False)
    kcal = db.Column(db.Float, nullable=False)
    is_deleted = db.Column(db.Boolean, nullable=False)
    portion_size = db.Column(db.Integer)
    last_used = db.Column(db.Date)
    ingredient_only = db.Column(db.Boolean, nullable=False)


class Dish(AbstractObject):
    __tablename__ = 'fit_dish'

    name = db.Column(db.String, nullable=False)
    out_of_stock = db.Column(db.Boolean, nullable=False)
    recipe = db.Column(db.String, nullable=False)
    last_used = db.Column(db.Date)
    for_dish = db.Column(db.Integer)


class DishIngredient(AbstractObject):
    __tablename__ = 'fit_dish_ingredient'

    dish_id = db.Column(db.Integer, nullable=False)
    food_id_ingredient = db.Column(db.Integer)
    dish_id_ingredient = db.Column(db.Integer)
    amount = db.Column(db.Integer, nullable=False)


class Meal(AbstractObject):
    __tablename__ = 'fit_meal'

    dish_id = db.Column(db.Integer)
    food_id = db.Column(db.Integer)
    amount = db.Column(db.Integer, nullable=False)
    meal_group_id = db.Column(db.Integer, nullable=False)
    calc_proteins = db.Column(db.Float, nullable=False)
    calc_fats = db.Column(db.Float, nullable=False)
    calc_carbs = db.Column(db.Float, nullable=False)
    calc_kcal = db.Column(db.Float, nullable=False)


class MealGroup(AbstractObject):
    __tablename__ = 'fit_meal_group'

    user_id = db.Column(db.Integer, nullable=False)
    day = db.Column(db.Date, nullable=False)
    meal_order_id = db.Column(db.Integer, nullable=False)
    meal_name = db.Column(db.String)


class MealOrder(AbstractObject):
    __tablename__ = 'fit_meal_order'

    name = db.Column(db.String, unique=True, nullable=False)
    ordering = db.Column(db.Integer, nullable=False)


class Equipment(AbstractObject):
    __tablename__ = 'gym_equipment'

    name = db.Column(db.String, nullable=False)


class TrainingPlans(AbstractObject):
    __tablename__ = 'gym_training_plans'

    name = db.Column(db.String, nullable=False, unique=True)


class TrainingJournal(AbstractObject):
    __tablename__ = 'gym_training_journal'

    training_plan_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    training_program_id = db.Column(db.Integer)


class TrainingPlanComponents(AbstractObject):
    __tablename__ = 'gym_training_plan_components'

    training_plan_id = db.Column(db.Integer, nullable=False)
    superset_id = db.Column(db.Integer, nullable=False)
    exercise_id = db.Column(db.Integer, nullable=False)


class Exercises(AbstractObject):
    __tablename__ = 'gym_exercises'

    equipment_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String, nullable=False, unique=True)
    weights_quantity = db.Column(db.Integer, nullable=False)


class ExerciseGroups(AbstractObject):
    __tablename__ = 'gym_exercise_groups'

    name = db.Column(db.String, nullable=False)


class Grouping(AbstractObject):
    __tablename__ = 'gym_grouping'

    exercise_id = db.Column(db.Integer, nullable=False)
    group_id = db.Column(db.Integer, nullable=False)


class TrainingDetails(AbstractObject):
    __tablename__ = 'gym_training_details'

    set_num = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    repetitions = db.Column(db.Integer, nullable=False)
    training_plan_component_id = db.Column(db.Integer, nullable=False)
    training_journal_id = db.Column(db.Integer, nullable=False)


class Supersets(AbstractObject):
    __tablename__ = 'gym_supersets'

    superset_id = db.Column(db.Integer, nullable=False)
    exercise_id = db.Column(db.Integer, nullable=False)


class TrainingPrograms(AbstractObject):
    __tablename__ = 'gym_training_programs'

    name = db.Column(db.String, nullable=False)


class TrainingProgramComponents(AbstractObject):
    __tablename__ = 'gym_training_program_components'

    training_plan_id = db.Column(db.Integer, nullable=False)
    training_program_id = db.Column(db.Integer, nullable=False)


class UserId(AbstractObject):
    __tablename__ = 'user_id'

    user_id = db.Column(db.String, nullable=False)
