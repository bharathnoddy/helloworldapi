from flask import Flask
from flask import request
from flask_restful import Resource, Api
import pymysql
import json
from datetime import date
import configparser


config = configparser.ConfigParser()
config.read('config.ini')

db_host = config['DEFAULT']['dbhost']
db_user = config['DEFAULT']['dbuser']
db_pass = config['DEFAULT']['dbpass']
db_name = config['DEFAULT']['dbname']


today = date.today()
### DB connection
db = pymysql.connect(db_host,db_user,db_pass,db_name)

app = Flask(__name__)
api =  Api(app)

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route('/hello/<username>', methods = ['POST' , 'GET'])

########Post request code

def api_message(username):
    if request.method == 'POST' and username.isalpha():
        dob = request.json['dob']
        sql = "SELECT * from username where username='"+username+"'"
        cursor = db.cursor() # connect to database
        result = cursor.execute(sql)

####If username is a new entry
        if result == 0:
            sql = 'INSERT INTO  username (username , dob ) VALUES (%s, %s)'
            val = (username , dob)
            cursor = db.cursor()
            cursor.execute(sql, val)
            db.commit()
            #message = "Filed with username "+username+" added to the DB"
            return('', 204)
## If username exists the update
        else:
            sql = 'REPLACE INTO  username (username , dob ) VALUES (%s, %s)'
            val = (username , dob)
            cursor = db.cursor()
            cursor.execute(sql, val)
            db.commit()
            #message = "Filed with username "+username+" Altered"
            return('', 204)

### GET request Code
    elif request.method == 'GET' and username.isalpha():
        dob = request.json['dob']
        sql = "SELECT * from username where username='"+username+"'"
        cursor = db.cursor() # connect to database
        var = cursor.execute(sql)
        if var == 1 :
            result = cursor.fetchall()
            for row in result:
                final = str(row[1])
            year,  month, day = final.split('-')
            date_of_birth = date(int(year), int(month) , int(day))
            birthday = date(today.year, date_of_birth.month, date_of_birth.day)
            days_until_birthday = (birthday-today).days
            if days_until_birthday > 0:
                message = "Hello, "+username+" ! Your Birthday is in "+str(days_until_birthday)+" days"
                return(json.dumps({ "message": message }))
            elif days_until_birthday == 0:
                message = "Hello, "+username+" ! Your Birthday!"
                return(json.dumps({ "message": message }))
            else:
                days_until_birthday = 365 + days_until_birthday
                message = "Hello, "+username+" ! Your Birthday is in "+str(days_until_birthday)+" days"
                return(json.dumps({ "message": message }))
        else:
            message = "Username "+username+" does not exist in the database!"
            return(json.dumps({ "message": message }))



    else:

        return(json.dumps( "message : The Operation is not defined or the username is incorrect. If its a legit activity then please put a feature request"))
