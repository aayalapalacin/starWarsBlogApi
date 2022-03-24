"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planets, Vehicle, People
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = "super-duper-secret"  
jwt = JWTManager(app)
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def get_users():
    users = User.query.all()
    users = [user.serialize() for user in users]

    return jsonify(users), 200

@app.route('/people', methods= ['GET'])
def get_peoples():
    peoples = People.query.all()
    peoples = [people.serialize() for people in peoples]

    return jsonify(peoples), 200

@app.route('/vehicle', methods = ['GET'])
def get_vehicles():
    vehicles = Vehicle.query.all()
    vehicles = [vehicle.serialize() for vehicle in vehicles]

    return jsonify(vehicles), 200

@app.route('/planet', methods=['GET'])
def get_planets():
    planets = Planets.query.all()
    planets= [planet.serialize() for planet in planets]

    return jsonify(planets), 200

@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    
    user = User.query.filter_by(email=username).one_or_none()
    if user is not None:
        if password == user.password:
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token)

    return jsonify({"msg": "Bad username or password"}), 401

    

@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
