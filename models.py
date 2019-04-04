from flask_sqlalchemy import SQLAlchemy

class Restaurant(db.Model):
    """
    Table schema for data to input into database
    """
    __tablename__ = "restaurant_info"
    id = db.Column(db.Integer, primary_key =True)
    camis = db.Column(db.Integer, Nullable=False)
    name = db.Column(db.String, Nullable=False)
    borough = db.Column(db.String, Nullable=False)
    building = db.Column(db.String, Nullable=False)
    street = db.Column(db.String, Nullable=False)
    zipcode = db.Column(db.Integer, Nullable=False)
    phone = db.Column(db.Integer, Nullable=False)
    cuisine = db.Column(db.String, Nullable=False)
    inspection_date = db.Column(db.Date)
    action = db.Column(db.String)
    violation_code = db.Column(db.String)
    critical_flag = db.Column(db.String)
    score = db.Column(db.Integer)
    grade = db.Column(db.String)
    grade_date = db.Column(db.Date)
    record_date = db.Column(db.Date)
    inspection_type = db.Column(db.String)

    def __init__(self, camis, name, borough, building, street,
                    zipcode, phone, cuisine, inspection_date, action,
                    violation_code, critical_flag, score, grade, grade_date,
                    record_date, inspection_type):
        self.camis = camis
        self.name = name
        self.borough = borough
        self.building = building
        self.street = street
        self.zipcode = zipcode
        self.phone = phone
        self.cuisine = cuisine
        self.inspection_date = inspection_date
        self.action = action
        self.violation_code = violation_code
        self.critical_flag = critical_flag
        self.score = score
        self.grade = grade
        self.grade_date = grade_date
        self.record_date = record_date
        self.inspection_type = inspection_type
