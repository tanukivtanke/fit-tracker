from base import app, db
from flask import render_template, request, jsonify
from objects.tables import User, Equipment, TrainingPlans, Exercises, TrainingPlanComponents, TrainingJournal, \
    TrainingDetails, Supersets, Grouping, ExerciseGroups, TrainingPrograms, TrainingProgramComponents

from util import list_to_json, string_to_date, calc_from_food, calc_from_dish, list_to_dict, get_argument

from auth import *


@app.route('/gym')
def gym():
    return render_template('gym.html')


@app.route('/api/gym/all_static')
def get_all_gym_static():
    return jsonify({
        "users": User.all_dict(),
        "equipment": Equipment.all_dict(),
        "exercises": Exercises.all_dict(),
        "exercise_groups": ExerciseGroups.all_dict(),
        "grouping": Grouping.all_dict(),
        "supersets": Supersets.all_dict(),
        "training_plan_components": TrainingPlanComponents.all_dict(),
        "training_plans": TrainingPlans.all_dict(),
        "training_program_components": TrainingProgramComponents.all_dict(),
        "training_programs": TrainingPrograms.all_dict()
    })

@app.route('/api/gym/equipment')
def get_equipment():
    return Equipment.all_json()


@app.route('/api/gym/training_plans')
def get_training_plans():
    return TrainingPlans.all_json()


@app.route('/api/gym/exercises')
def get_exercises():
    return Exercises.all_json()


@app.route('/api/gym/curr_user', methods=['POST'])
def get_curr_user():
    received_data = request.json
    user_data = User.find(username=received_data)
    return user_data.json()


@app.route('/api/gym/all')
def get_all_gym():
    return jsonify({
        "user": User.all_dict(),
        "training_plans": TrainingPlans.all_dict(),
        "training_plan_components": TrainingPlanComponents.all_dict(),
        "training_journal": TrainingJournal.all_dict(),
        "training_details": TrainingDetails.all_dict(),
        "supersets": Supersets.all_dict(),
        "grouping": Grouping.all_dict(),
        "exercises": Exercises.all_dict(),
        "exercise_groups": ExerciseGroups.all_dict(),
        "equipment": Equipment.all_dict(),
        "training_programs": TrainingPrograms.all_dict(),
        "training_program_components": TrainingProgramComponents.all_dict()
    })
