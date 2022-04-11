from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import mysql.connector
import os

# Init app
app = Flask(__name__)
#basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:murtazahaider@localhost/Demo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)

# Init ma
ma = Marshmallow(app)

# Product Class/Model
class Product(db.Model):
    __tablename__ = 'ProjectDP'
    ID = db.Column(db.Integer, primary_key=True)
    City = db.Column(db.String(50), unique=True)
    Sunshine = db.Column(db.Integer)
    Cost_water = db.Column(db.Float)
    ObesityLevels_percent = db.Column(db.Float)
    Life_expectancy = db.Column(db.Float)
    Pollution_Index = db.Column(db.Float)
    Hours_worked = db.Column(db.Integer)
    Happiness_levels = db.Column(db.Float)
    Outdoor_activities = db.Column(db.Integer)
    Takeout_places = db.Column(db.Integer)
    Gym_membership = db.Column(db.Float)

    def __init__(self, ID, City, Sunshine, Cost_water, ObesityLevels_percent, Life_expectancy, Pollution_Index, Hours_worked, Happiness_levels, Outdoor_activities, Takeout_places, Gym_membership):
        self.ID = ID
        self.City = City
        self.Sunshine = Sunshine
        self.Cost_water = Cost_water
        self.ObesityLevels_percent = ObesityLevels_percent
        self.Life_expectancy = Life_expectancy
        self.Pollution_Index = Pollution_Index
        self.Hours_worked = Hours_worked
        self.Happiness_levels = Happiness_levels
        self.Outdoor_activities = Outdoor_activities
        self.Takeout_places = Takeout_places
        self.Gym_membership = Gym_membership

# Product Schema
class ProductSchema(ma.Schema):
  class Meta:
    fields = ('ID', 'City', 'Sunshine', 'Cost_water', 'ObesityLevels_percent', 'Life_expectancy', 'Pollution_Index', 'Hours_worked', 'Happiness_levels', 'Outdoor_activities', 'Takeout_places', 'Gym_membership')

# Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Get Single Products
@app.route('/product/<id>', methods=['GET'])
def get_product(id):
  product = Product.query.get(id)
  return product_schema.jsonify(product)

# Run Server
if __name__ == '__main__':
  app.run(debug=True)