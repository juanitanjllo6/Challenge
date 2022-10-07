from flask import Flask, request,jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from config import settings
import json
import psycopg2
import requests


url_db = settings.database_url

try:
        db_connect = create_engine(url_db)
        print("Database opened successfully")
except:
        print ("I am unable to connect to the database")
 
conn = db_connect.connect()
app = Flask(__name__)
api = Api(app)

class Persons(Resource):
    def get(self):
        conn = db_connect.connect() 
        query = conn.execute("select * from Persons")
        return {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor.fetchall()]}

class Data(Resource):
    def get(self, id):
        conn = db_connect.connect()
        query = conn.execute("select * from Persons where id ='%d' " % int(id))
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)

api.add_resource(Persons, '/data')
api.add_resource(Data, '/data/<id>') 
if __name__ == '__main__':
     app.run(port='8080')      