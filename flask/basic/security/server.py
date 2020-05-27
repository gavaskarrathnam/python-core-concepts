from flask import Flask
from models import db, User
from api import api, Users, Resources, Token

app = Flask(__name__)
app.config.from_pyfile('settings.cfg')

db.init_app(app)
api.init_app(app)

api.prefix = app.config["BASE_API_URL"]

# Endpoints
api.add_resource(Resources, "/resource/<string:username>")
api.add_resource(Users, "/users", "/users/<int:id>")
api.add_resource(Token, "/token")

if __name__ == '__main__':
    app.run(debug=True)
