from flask import Flask, request,jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from dotenv import load_dotenv
from config import settings
import json
import psycopg2
import requests


url_db = settings.database_url
url = 'https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios'
data = requests.get(url)
datajson = {}
if data.status_code == 200:
    datajson = data.json()
    try:
        db_connect = create_engine(url_db)
        print("Database opened successfully")
    except:
        print ("I am unable to connect to the database")
 
conn = db_connect.connect()
app = Flask(__name__)
api = Api(app)

class Create(Resource):
    def get(self):
        conn = db_connect.connect()
        try:
            conn.execute('''CREATE TABLE tasks8
            (fec_alta VARCHAR(50),
            user_name VARCHAR(50),
            codigo_zip VARCHAR(50),
            credit_card_num VARCHAR(50),
            credit_card_ccv VARCHAR(50),
            cuenta_numero VARCHAR(50),
            direccion VARCHAR(50),
            geo_latitud VARCHAR(50),
            geo_longitud VARCHAR(50),
            color_favorito VARCHAR(50),
            foto_dni VARCHAR(80),
            ip VARCHAR(50),
            auto VARCHAR(50),
            auto_modelo VARCHAR(50),
            auto_tipo VARCHAR(50),
            auto_color VARCHAR(50),
            cantidad_compras_realizadas INT,
            avatar VARCHAR(80),
            fec_birthday VARCHAR(50),
            id VARCHAR(50) PRIMARY KEY);''')
            return {"Message": "Table created successfully"}
        except Exception as error:
            return {"Message": "Table already exists"}

class Insert(Resource):
    def get(self):
        conn = db_connect.connect() 
        try:
            conn.execute("INSERT INTO tasks8(id,fec_alta,user_name,codigo_zip,credit_card_num,credit_card_ccv,cuenta_numero,direccion,geo_latitud,geo_longitud,color_favorito,foto_dni,ip,auto,auto_modelo,auto_tipo,auto_color,cantidad_compras_realizadas,avatar,fec_birthday) VALUES(%(id)s, %(fec_alta)s, %(user_name)s, %(codigo_zip)s, %(credit_card_num)s, %(credit_card_ccv)s, %(cuenta_numero)s, %(direccion)s, %(geo_latitud)s, %(geo_longitud)s, %(color_favorito)s, %(foto_dni)s, %(ip)s, %(auto)s, %(auto_modelo)s, %(auto_tipo)s, %(auto_color)s, %(cantidad_compras_realizadas)s, %(avatar)s, %(fec_birthday)s)",datajson)
            return {"Message":"Record inserted successfully"}
        except Exception as error:
            return {"Message": "Record already inserted "}

class Tasks(Resource):
    def get(self):
        conn = db_connect.connect() 
        query = conn.execute("select * from tasks8")
        return {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor.fetchall()]}

class Data(Resource):
    def get(self, id):
        conn = db_connect.connect()
        query = conn.execute("select * from tasks8 where id ='%d' " % int(id))
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)

api.add_resource(Create, '/create')
api.add_resource(Insert, '/insert')
api.add_resource(Tasks, '/tasks')
api.add_resource(Data, '/tasks/<id>') 
if __name__ == '__main__':
     app.run(port='8080')      