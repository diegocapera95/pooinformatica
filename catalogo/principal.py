from flask import Flask, render_template
from fabricas import *
from random import choice

app = Flask(__name__)


@app.route('/')
def principal():
    fabricas = [FabricaHumanos(), FabricaOrcos()]
    fabrica = choice(fabricas)
    arma = fabrica.crear_arma()
    escudo = fabrica.crear_escudo()
    montura = fabrica.crear_montura()
    cuerpo = fabrica.crear_cuerpo()

    productos = []

    productos.append(arma)
    productos.append(escudo)
    productos.append(montura)
    productos.append(cuerpo)

    return render_template("productos.html", productos = productos)

if __name__ == '__main__':
    app.run(debug=True)
