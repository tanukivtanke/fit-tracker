from flask import jsonify

from base import db


class AbstractObject(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def __repr__(self):
        fields = ', '.join([f"{key}={value!r}" for key, value in self.dict().items()])
        return f"{self.__class__.__name__}({fields})"

    def dict(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}

    def json(self):
        return jsonify(self.dict())