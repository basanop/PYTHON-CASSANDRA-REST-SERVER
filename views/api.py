from functools import wraps
import json
from cassandra.cqlengine import connection
from flask import Blueprint, Response
import flask

from dao.db import CassandraDBConnector
import util

__author__ = 'puneet'

api = Blueprint("api",__name__)

db = CassandraDBConnector()
db.connect("127.0.0.1","1234")

def json_api(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        result = f(*args, **kwargs)      # call function
        json_result = util.to_json(result)
        return Response(response=json_result, 
                        status = 200, 
                        mimetype='application/json')
    return decorated_function

@api.route('/', defaults={"path": ""})
@api.route('/<path:path>')
def index(path=None):
    return "Hello World"

@api.route("/user", methods=["POST"])
@json_api
def get_user():
    data = json.loads(flask.request.data)
    iid  = data.get('id',None)
    email = data.get('email',None)
    
    if iid is None or email is None:
        return {"error": "Invalid Input"}
        
    if iid:
        result = db.query("SELECT * FROM user_by_id where id={}".format(iid));

    if email:
        result = db.query("SELECT * FROM user_by_email where email='{}'".format(email));
    res = {}

    if result is None:
        row['error'] = "No User Present"

    for row in result:
        res['id'] = row.id
        res['first_name'] = row.first_name
        res['second_name'] = row.last_name
        res['email']       = row.email

    return res

@api.route("/users", methods=["POST"])
@json_api
def get_users():
    data = json.loads(flask.request.data)
    city  = data.get('city',None)
    company = data.get('company',None)

    if company is None or city is None:
        return {"error": "Invalid Input"}
    
    result = db.query("SELECT * FROM USER_BY_COMPANY_CITY where company='{}' and city = '{}'".format(company, city))
    res = {}
    users = []
    if result is None:
        row['error'] = "No User Present"

    for row in result:
        users.append({
            "id": row.id,
            "first_name": row.first_name,
            "last_name" : row.last_name,
            "email"     : row.email
        })
    res['users'] = users
    return res

@api.route("/counts",methods=["POST"])
@json_api
def get_counts():
    data = json.loads(flask.request.data)
    domain = data.get('domain',None)
    city = data.get('city', None)

    if domain is None or city is None:
        return {"error": "Invalid Input"}
    
    result =  db.query("SELECT * FROM USER_BY_DOMAIN where domain='{}' and city = '{}'".format(domain, city))

    res = {}

    if result is None:
        res['error'] = "No Domain / City Present"

    for row in result:
        res['count'] = row.counter
    
    return res

@api.route("/activity", methods=["POST"])
@json_api
def activity_count():
    data = json.loads(flask.request.data)
    date = data.get('date', None)
    company  = data.get('company', None)

    if date is None or company is None:
        return {"error": "Invalid Input"}

    result = db.query("SELECT * FROM COUNT_ACTIVITY_BY_USER WHERE date='{}' and company='{}'".format(date,company))
    res = {}
    if result is None:
        res['error'] = "No Activity present"

    for row in result:
        res['count'] = row.counter

    return res

@api.route("/subscribe",methods=["POST"])
@json_api
def list_users():
    data = json.loads(flask.request.data)
    date = data.get('date', None)
    domain  = data.get('domain', None)
    event = data.get('event', None)

    if date is None or domain is None or event is None:
        return {"error": "Invalid Input"}

    result = db.query("SELECT * FROM ACTIVITY_BY_USER WHERE date='{}' and event='{}' and domain='{}'".format(date, event, domain))
    res = {}
    users = []
    if result is None:
        res['error'] = "No Result found"

    for row in result:
        users.append({
            "id": row.user_id
        })

    return {"users": users}

@api.route("/summary", methods=["POST"])
@json_api
def get_summary():
    data = json.loads(flask.request.data)
    date = data.get('date', None)
    company  = data.get('company', None)

    if date is None or company is None:
        return {"error": "Invalid Input"}
    
    result = db.query("SELECT * FROM ACTIVITY_BY_COMPANY WHERE company = '{}' and date='{}' ".format(company, date ))
    res = {}
    if result is None:
        res['error'] = "No Result found"
    
    for row in result:
        res['clicks'] = row.clicks
        res['orders'] = row.orders
        res['subscribes'] = row.subscribes
        res['views'] = row.views

    return res
