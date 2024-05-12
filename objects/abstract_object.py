from flask import jsonify

from base import db, app


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

    @classmethod
    def all_json(cls):
        all_objs = cls.query.all()
        return jsonify([i.dict() for i in all_objs])

    @classmethod
    def all(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()

    @classmethod
    def find(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()

    def save(self):
        with app.app_context():
            db.session.add(self)
            db.session.commit()
            db.session.refresh(self)

    def update(self):
        with app.app_context():
            db.session.merge(self)
            db.session.commit()

    @classmethod
    def delete_by_id(cls, obj_id):
        with app.app_context():
            obj = cls.find(id=obj_id)
            if obj:
                db.session.delete(obj)
                db.session.commit()
                return True
            else:
                return False
