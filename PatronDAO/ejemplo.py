from xml.dom import minidom
doc = minidom.parse("datos.xml")
nombre = doc.getElementsByTagName("nombre")[0]
print(nombre.firstChild.data)
empleados = doc.getElementsByTagName("producto")
for empleado in empleados:
    sid = empleado.getAttribute("id")
    username = empleado.getElementsByTagName("nombre")[0]
    password = empleado.getElementsByTagName("descripcion")[0]
    print("id:%s " % sid)
    print("username:%s" % username.firstChild.data)
    print("password:%s" % password.firstChild.data)


    
'''
def cargar_datos(ruta):
    with open(ruta) as contenido:
        resultado = json.load(contenido)
        for resultad in resultado:
            if resultad.get('tipo')=='computador':
                print(resultad.get('tipo'))
            else:
                print(resultad.get('nombre'))


if __name__ == '__main__':
    ruta = 'Data/data.json'
    cargar_datos(ruta)
'''