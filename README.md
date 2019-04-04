# restaurant-simple
An app with an ETL pipeline for New York City Restaurant Inspection Data to help a germaphobe friend who loves Thai, but won't eat somewhere with a rating less than B. I have two views for them:
- '/' renders a template to returns results to this requirement, displaying restaurant names and their grades
-  '/curl' returns a JSON list, where each result (restaurant) is its own dictionary with all columns. 

Health Inspection Data CSV:
https://data.cityofnewyork.us/api/views/43nn-pn8j/rows.csv?accessType=DOWNLOAD

## CURL Request
To curl results from the SQL Query, type in: 
- curl https://pickly-thai-lover.herokuapp.com/curl

## SQL Query
Raw SQL:
- '''SELECT * FROM restaurant_info WHERE (cuisine LIKE %Thai%) AND (grade in ('A', 'B'))'''

SQL Alchemy Query Used in Code:
- Restaurant.query.filter(and_(Restaurant.cuisine.like('%Thai%'), \
                        Restaurant.grade.in_(['A', 'B']))).all()



## Schema Design
- 
