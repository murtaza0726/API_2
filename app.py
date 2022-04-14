from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import mysql.connector
import os

# Init app
app = Flask(__name__)
#basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://be32eb4083c64f:b41f6242@us-cdbr-east-05.cleardb.net/heroku_16c301709b71772'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)

# Init ma
ma = Marshmallow(app)

# Health Class/Model
class Health(db.Model):
    __tablename__ = 'ProjectDP'
    ID = db.Column(db.Integer, primary_key=True)
    Country = db.Column(db.String(50), unique=True)
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

    def __init__(self, ID, Country, City, Sunshine, Cost_water, ObesityLevels_percent, Life_expectancy, Pollution_Index, Hours_worked, Happiness_levels, Outdoor_activities, Takeout_places, Gym_membership):
        self.ID = ID
        self.City = City
        self.Country = Country
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

# Health Schema
class HealthSchema(ma.Schema):
  class Meta:
    fields = ('ID', 'Country', 'City', 'Sunshine', 'Cost_water', 'ObesityLevels_percent', 'Life_expectancy', 'Pollution_Index', 'Hours_worked', 'Happiness_levels', 'Outdoor_activities', 'Takeout_places', 'Gym_membership')

# Init schema
health_schema = HealthSchema()
health_schema = HealthSchema(many=True)

# Get Single Products
@app.route('api/client/v0.1/api/data/id/<id>', methods=['GET'])
def get_health(id):
  health = Health.query.get(id)
  return health_schema.jsonify(health)

# Run Server
if __name__ == '__main__':
  app.run(debug=True)