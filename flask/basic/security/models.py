from flask_sqlalchemy import SQLAlchemy
from passlib.apps import custom_app_context as pwd_context # going to deprecate, use below version
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

# extensions
db = SQLAlchemy()  # ORM


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(32), index = True)
    password_hash = db.Column(db.String(128))

    # Password Hashing
    def hash_password(self, password):
        self.password_hash = pwd_context.hash(password)

    # Password verification
    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    # Generate auth token
    def generate_auth_token(self, secret_key, expiration=600):
        s = Serializer(secret_key, expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token, secret_key):
        s = Serializer(secret_key)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None # Valid token, but expired
        except BadSignature:
            return None # Invalid token
        user = User.query.get

        return user
