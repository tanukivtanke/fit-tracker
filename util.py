from flask import jsonify
from datetime import datetime


def list_to_json(obj: list):
    return jsonify([i.dict() for i in obj])


def string_to_date(string):
    return datetime.strptime(string, '%Y-%m-%d')
