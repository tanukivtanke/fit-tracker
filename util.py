from flask import jsonify


def list_to_json(obj: list):
    return jsonify([i.dict() for i in obj])

