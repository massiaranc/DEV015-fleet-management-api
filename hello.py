""" 
primer interacción
"""
from flask import Flask , jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import os
from dotenv import load_dotenv

load_dotenv()

class Base(DeclarativeBase):
    pass
#crea la app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")#CARGA LA URL DESDE .ENV


db = SQLAlchemy(model_class=Base)
db.init_app(app)



@app.route('/' , methods=['GET'])
def hello_world():
    """ devuelve un hola en la pag"""
    return jsonify(mensaje= "hola Mundo")

@app.route('/taxis')
def taxis():
    """ creacion de ruta taxis"""
    return 'Taxis'

if __name__ == '__main__':
    app.run(debug=True)
