# restaurant-simple
An app with an ETL pipeline for New York City Restaurant Inspection Data to help a germaphobe friend who loves Thai, but won't eat somewhere with a rating less than B. I have two views for them:
- '/' renders a template to returns results to this requirement, displaying restaurant names and their grades
-  '/curl' returns a JSON list, where each result (restaurant) is its own dictionary with all columns.

Health Inspection Data CSV:
https://data.cityofnewyork.us/api/views/43nn-pn8j/rows.csv?accessType=DOWNLOAD

## CURL Request
To curl results from the SQL Query:
- curl https://pickly-thai-lover.herokuapp.com/curl

## SQL Query
Raw SQL:
- '''SELECT * FROM restaurant_info WHERE (cuisine LIKE %Thai%) AND (grade IN ('A', 'B'))'''

SQL Alchemy Query Used in Code:
- Restaurant.query.filter(and_(Restaurant.cuisine.like('%Thai%'), \
                        Restaurant.grade.in_(['A', 'B']))).all()



## App Design
- app
  - templates
    - index.html
    - results.html
  - app.py
  - extracttransform.py
  - tests.py
- Procfile
- README.md
- requirements.txt
- runtime.txt

## Database Design
- Heroku Postgres DB
  - restaurant_info
    - id : int, primary_key
    - camis : int
    - name : string, nullable=False
    - borough : string
    - building : string
    - street : string
    - zipcode : int
    - phone : bigint
    - cuisine : string
    - inspection_date : date
    - action : string
    - violation_code : string
    - critical_flag : string
    - score : int
    - grade : string
    - grade_date : date
    - record_date : date
    - inspection_type : string

## Decisions
- Overall Approach
  - I wanted to take the easiest to read and understand approach. I have developed in Flask before, but have not used Heroku, so I wanted to incorporate a framework that I felt comfortable in. I put everything in app.py because I only had one model and two simple views, so I thought it was small enough to put under one roof. I made populate_db() as only an if statement, so that it would only populate my database table if it was empty.
- Extract Transform
  - I use pandas everyday at work, but it requires a lot of overhead and I wanted to challenge myself to use a native data structure that is quickly mutable. I chose dictionaries specifically, because it mocks the structure of a model instance.
  - I put it into a class because it was very self-contained into performing functions that did not interact with the database. I developed the extract and transform class and tested it manually a lot and once I got the output I wanted, I knew that it could interact with the add_rows function.
- CURL and View
  - I am a visual person, so I wanted to visualize what the request could look like rather than looking at only the JSONify-ed return, also since Heroku gives you a URL, I wanted to use it in the most basic way!

## Next Steps
- write more tests!!!
  - create tests that test adding to db
  - create tests for SQL queries
- app schema 2.0
  - given more time, I would love to separate the app to have config.py, models.py, views.py etc rather than house it all in app.py
- create a frontend that allows you to choose between options and generates queries
- optimizing the extract, transform, and load process
  - each of these steps requires a for loop that runs over each element, I think that my process could be optimized both in terms of space and time
- be clear about data consistency
  - some restaurants don't have complete data --> how are these handled?
    - don't include in DB
    - make it clear that restaurants without grades will not show up with queries?
