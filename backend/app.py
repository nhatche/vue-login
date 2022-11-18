from flask import Flask, jsonify, request
from flask_cors import CORS

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)

@app.route("/token", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    print('username:', username, '\n password:', password)

    if username != "test@gmail.com" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

stores = [
  {
    "name": "nhatche",
    "age": 18
  }
]

app.config['SQL_DATABASE_URL'] = 'mysql://root:quangnhat@0935467013@localhost/users'

@app.route('/')
def base_route():
  return '<h1>Welcome base route</h1>'

@app.route('/login')
def login_route():
  return '<h1>Login page</h1>'

@app.route('/token', methods = ['POST'])
def update_text():
  return jsonify(token = "this is token",)

@app.get('/store')
def get_store():
  return stores

if __name__ == '__main__':
  app.run(debug=True, port=4000)
