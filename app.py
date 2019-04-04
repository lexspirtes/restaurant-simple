from flask import Flask, render_template, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_
import sys
import json
from flask.ext.heroku import Heroku
from extracttransform import Etl

app = Flask( __name__ )
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Lex@localhost:5432/restaurant'
heroku = Heroku(app)
db = SQLAlchemy(app)

class Restaurant(db.Model):
    """
    Table schema for data to input into database
    """
    __tablename__ = "restaurant_info"
    id = db.Column(db.Integer, primary_key =True)
    camis = db.Column(db.Integer)
    name = db.Column(db.String, nullable=False)
    borough = db.Column(db.String)
    building = db.Column(db.String)
    street = db.Column(db.String)
    zipcode = db.Column(db.Integer)
    phone = db.Column(db.BigInteger)
    cuisine = db.Column(db.String)
    inspection_date = db.Column(db.Date)
    action = db.Column(db.String)
    violation_code = db.Column(db.String)
    critical_flag = db.Column(db.String)
    score = db.Column(db.Integer)
    grade = db.Column(db.String)
    grade_date = db.Column(db.Date)
    record_date = db.Column(db.Date)
    inspection_type = db.Column(db.String)

    @property
    def stringify(self):
        column_list = ['camis', 'name', 'borough', 'building',
                        'street', 'zipcode', 'phone', 'cuisine',
                        'inspection_date', 'action', 'violation_code',
                        'critical_flag', 'score', 'grade', 'grade_date',
                        'record_date', 'inspection_type']
        return dict((c, getattr(self, c)) for c in column_list)

#function that adds all rows to database
def add_rows(data_list):
    data_length = len(data_list)
    rows_added = 0
    for row in data_list:
        current_row = Restaurant(
        building=row['building'],
        critical_flag=row['critical_flag'],
        camis=row['camis'],
        name=row['dba'],
        borough=row['boro'],
        street=row['street'],
        zipcode=row['zipcode'],
        phone=row['phone'],
        cuisine=row['cuisine_description'],
        inspection_date=row['inspection_date'],
        action=row['action'],
        violation_code=row['violation_code'],
        score=row['score'],
        grade=row['grade'],
        grade_date=row['grade_date'],
        record_date=row['record_date'],
        inspection_type=row['inspection_type'])
        db.session.add(current_row)
        db.session.commit()
        rows_added +=1
    print('percentage of rows added to db: ' + \
            str(int(rows_added/data_length) * 100) + '%')

def populate_db():
    if Restaurant.query.first() == None:
        restaurant_data = Etl()
        add_rows(restaurant_data.data)

populate_db()

@app.route('/', methods=['GET'])
def return_results():
    """
    returns results to query: thai food with a health department rating
    greater than a B
    """
    #run thing to check if db is populated?
    #query that has been asked for
    restaurant_info = Restaurant.query.filter(and_(Restaurant.cuisine.like('%Thai%'), \
                        Restaurant.grade.in_(['A', 'B']))).all()
    return render_template("results.html", restaurant_info=restaurant_info)

@app.route('/curl', methods=['GET'])
def json_me():
    """
    returns results to query: thai food with a health department rating as a json object
    """
    #run thing to check if db is populated?
    #query that has been asked for
    restaurant_info = Restaurant.query.filter(and_(Restaurant.cuisine.like('%Thai%'), \
                        Restaurant.grade.in_(['A', 'B']))).all()
    return jsonify(data =[r.stringify for r in restaurant_info])

if __name__ == '__main__':
    app.debug = True
    app.run()
