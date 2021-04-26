from flask import Flask, render_template
from fabricas import *
from random import choice
import json
import xml.etree.ElementTree as ET
from xml.dom import minidom
app = Flask(__name__)

@app.route('/')

def principal():
    print("¿Cómo desea cargar los datos? 1=JSON,2=XML")
    carga = input()
    if carga=='1':
        ruta = 'Data/data.json'
        fabricas = [FabricaGeneral()]
        fabrica = choice(fabricas)
        productos = []
        with open(ruta) as contenido:
            resultado = json.load(contenido)
            for resultad in resultado:
                if resultad.get('tipo')=='computador':
                    Computador= fabrica.crear_computador(resultad.get('nombre'),resultad.get('descripcion'))
                    productos.append(Computador)
                else:
                    Partes = fabrica.crear_partes(resultad.get('nombre'),resultad.get('descripcion'))
                    productos.append(Partes)   
        return render_template("productos.html", productos = productos)      
    else:
        fabricas = [FabricaGeneral()]
        fabrica = choice(fabricas)
        productos = []
        doc = minidom.parse("datos.xml")
        nombre = doc.getElementsByTagName("nombre")[0]
        print(nombre.firstChild.data)
        empleados = doc.getElementsByTagName("producto")
        for empleado in empleados:
            tipo=empleado.getElementsByTagName("tipo")[0]
            if tipo.firstChild.data=='computador':
                nombre=empleado.getElementsByTagName("nombre")[0]
                descripcion=empleado.getElementsByTagName("descripcion")[0]
                Computador= fabrica.crear_computador(nombre.firstChild.data, descripcion.firstChild.data)
                productos.append(Computador)
            else:
                nombre=empleado.getElementsByTagName("nombre")[0]
                descripcion=empleado.getElementsByTagName("descripcion")[0]
                Partes = fabrica.crear_partes(nombre.firstChild.data, descripcion.firstChild.data)
                productos.append(Partes)
        return render_template('productos.html', productos = productos)

if __name__ == '__main__':
    app.run(debug=True)

