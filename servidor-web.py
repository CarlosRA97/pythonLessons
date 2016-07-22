from flask import Flask
from flask import render_template
from ventilador import Ventilador
from luces import Luces

app = Flask(__name__)

home = "/home"
fan_route = home + "/fan"
light_route = home + "/light"


v = Ventilador()
l = Luces()


@app.route('/')
@app.route(home)
def home():
    # Proceso de python

    # Mostrar la pagina web
    return render_template('home.html', fan_route=fan_route, light_route=light_route)

@app.route(fan_route)
def fan():
    return render_template('fan.html', velocidad=v.velocidad, temporizador=v.temporizador, luz_estado=v.luz_on_off, ventilador_estado=v.ventilador_on_off, back=home)

@app.route(light_route)
def light():
    return render_template('light.html', luz_estado=l.luz_estado, luz_potencia=l.luz_potencia, back=home)