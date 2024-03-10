from base import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        fields = ', '.join([f"{key}={value!r}" for key, value in self.__dict__.items() if not key.startswith("_")])
        return f"{self.__class__.__name__}({fields})"
