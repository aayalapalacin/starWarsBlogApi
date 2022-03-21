from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorite_people = db.relationship("FavoritePeople")

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "favorite_people": self.favorite_people

            # do not serialize the password, its a security breach
        }
class People(db.Model):
    """
    name string -- The name of this person.
birth_year string -- The birth year of the person, using the in-universe standard of BBY or ABY - Before the Battle of Yavin or After the Battle of Yavin. The Battle of Yavin is a battle that occurs at the end of Star Wars episode IV: A New Hope.
eye_color string -- The eye color of this person. Will be "unknown" if not known or "n/a" if the person does not have an eye.
gender string -- The gender of this person. Either "Male", "Female" or "unknown", "n/a" if the person does not have a gender.
hair_color string -- The hair color of this person. Will be "unknown" if not known or "n/a" if the person does not have hair.
height string -- The height of the person in centimeters.
mass string -- The mass of the person in kilograms.
skin_color string -- The skin color of this person.
homeworld string -- The URL of a planet resource, a planet that this person was born on or inhabits.
films array -- An array of film resource URLs that this person has been in.
species array -- An array of species resource URLs that this person belongs to.
starships array -- An array of starship resource URLs that this person has piloted.
vehicles array -- An array of vehicle resource URLs that this person has piloted.
url string -- the hypermedia URL of this resource.
created string -- the ISO 8601 date format of the time that this resource was created.
edited string -- the ISO 8601 date format of the time that this resource was edited.
        """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    birth_year = db.Column(db.String(50), unique=False, nullable=True)
    eye_color = db.Column(db.String(20), unique=False, nullable=True)
    gender = db.Column(db.String(20), unique=False, nullable=True)
    hair_color = db.Column(db.String(20), unique=False, nullable=True)
    height = db.Column(db.Integer, unique=False, nullable=False)
    mass = db.Column(db.String(20), unique=False, nullable=True)


    
    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "height": self.height,
            "mass": self.mass,
       
        }

    
class Vehicle(db.Model):
        # name string -- The name of this vehicle. The common name, such as "Sand Crawler" or "Speeder bike".
        # model string -- The model or official name of this vehicle. Such as "All-Terrain Attack Transport".
        # vehicle_class string -- The class of this vehicle, such as "Wheeled" or "Repulsorcraft".
        # manufacturer string -- The manufacturer of this vehicle. Comma separated if more than one.
        # length string -- The length of this vehicle in meters.
        # cost_in_credits string -- The cost of this vehicle new, in Galactic Credits.
        # crew string -- The number of personnel needed to run or pilot this vehicle.
        # passengers string -- The number of non-essential people this vehicle can transport.
        # max_atmosphering_speed string -- The maximum speed of this vehicle in the atmosphere.
        # cargo_capacity string -- The maximum number of kilograms that this vehicle can transport.
        # consumables *string
        # The maximum length of time that this vehicle can provide consumables for its entire crew without having to resupply.
        # films array -- An array of Film URL Resources that this vehicle has appeared in.
        # pilots array -- An array of People URL Resources that this vehicle has been piloted by.
        # url string -- the hypermedia URL of this resource.
        # created string -- the ISO 8601 date format of the time that this resource was created.
        # edited string -- the ISO 8601 date format of the time that this resource was edited.
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    model = db.Column(db.String(100), unique=False, nullable=True)
    vehicle_class = db.Column(db.String(100), unique=False, nullable=True)

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "vehicle_class": self.vehicle_class,
        }

    
class Planets(db.Model):
        # name string -- The name of this planet.
        # diameter string -- The diameter of this planet in kilometers.
        # rotation_period string -- The number of standard hours it takes for this planet to complete a single rotation on its axis.
        # orbital_period string -- The number of standard days it takes for this planet to complete a single orbit of its local star.
        # gravity string -- A number denoting the gravity of this planet, where "1" is normal or 1 standard G. "2" is twice or 2 standard Gs. "0.5" is half or 0.5 standard Gs.
        # population string -- The average population of sentient beings inhabiting this planet.
        # climate string -- The climate of this planet. Comma separated if diverse.
        # terrain string -- The terrain of this planet. Comma separated if diverse.
        # surface_water string -- The percentage of the planet surface that is naturally occurring water or bodies of water.
        # residents array -- An array of People URL Resources that live on this planet.
        # films array -- An array of Film URL Resources that this planet has appeared in.
        # url string -- the hypermedia URL of this resource.
        # created string -- the ISO 8601 date format of the time that this resource was created.
        # edited string -- the ISO 8601 date format of the time that this resource was edited.

    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(50),unique=True,nullable=False)
    diameter = db.Column(db.String (30), unique=False, nullable=True)

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
        }


class FavoritePeople(db.Model):
    user_id = db.Column(db.ForeignKey('user.id'), primary_key=True)
    people_id = db.Column(db.ForeignKey('people.id'), primary_key=True)
    child = db.relationship("People")

   
