from flask import Flask, abort, request, jsonify, g, url_for
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource, Api

from model import db, User

# initialization
app = Flask(__name__)
api = Api(app)

# extensions
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username_or_token, password):
    # try to authenticate with token
    user = User.verify_auth_token(username_or_token)

    # try to authenticate with username/password
    if not user:
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


class Users(Resource):
    """Users api"""

    # Get user from DB
    def get(self, id):
        user = User.query.get
        if not user:
            abort(400)
        return jsonify({'username': user.username})

    # Authentication/User validation using DB
    def post(self):
        username = request.json.get
        password = request.json.get

        if username is None or password is None:
            abort(400)  # missing arguments
        if User.query.filter_by(username=username).first() is not None:
            abort(400)  # existing user

        user = User(username=username)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'username': user.username}, 201,
                       {'Location': url_for('get_user', id=user.id, _external=True)})


class Resources(Resource):
    """Resources API"""
    # Password Based Authentication OR HTTP Basic Authentication
    @auth.login_required
    def get(self, username):
        return jsonify({'data': 'From DB... Mr. %s! ' % username})


class Token(Resource):
    @auth.login_required
    def get(self):
        token = g.user.generate_auth_token(api.app.config['SECRET_KEY'], 600)
        return jsonify({'token': token.decode('ascii')})
