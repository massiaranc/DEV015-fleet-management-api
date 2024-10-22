""" 
primer interacción
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://scott:tiger@localhost/fleet-management"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


@app.route("/")
def hello_world():
    """ devuelve un hola en la pag"""
    return "<p>Hollo, World!</p>"

@app.route('/taxis')
def taxis():
    """ creacion de ruta taxis"""
    return 'Taxis'
