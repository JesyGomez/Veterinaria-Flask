from flask import Flask, render_template, request, redirect
from dataUser import *  
from controller_db import *  

app = Flask(__name__)

# Home
@app.route("/")
def dataHome():
    title = "Veterinaria Los Amigos!"
    return render_template('index.html', titulo=title, users=users)

# Error handler
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error=error), 404

# Mostrar detalles de un usuario
@app.route("/persona/<int:id>")
def dataUsers(id):
    title = "Staff"
    return render_template("persona.html", title=title, user=users[id])

# Contacto
@app.route('/contacto')
def dataContacto():
    title = "Contacto"
    return render_template("contacto.html", title=title)

# Tratamientos
@app.route('/tratamiento')
def getTratamientos():
    # tratamientos = obtener_tratamientos() 
    titulo = "Tratamientos"
    return render_template("tratamiento.html", title=titulo)

# Insertar nuevo tratamiento
@app.route("/tratamiento/cargar_producto")
def insertTratamiento():
    title = "Nuevo Tratamiento"
    return render_template("form_nuevo_tratamiento.html", title=title)

@app.route("/tratamiento/guardar_nuevo_tratamiento", methods=['POST'])
def newTratamiento():
    nombre_tratamiento = request.form['nombre']
    descripcion_tratamiento = request.form['descripcion']
    precio_tratamiento = request.form['precio']
    tipo_tratamiento = request.form['tipo'] 
    cargar_nuevo_tratamiento(nombre_tratamiento, descripcion_tratamiento, precio_tratamiento, tipo_tratamiento)
    return redirect("/tratamiento")

# Editar tratamiento
@app.route("/tratamiento/editar_producto/<int:id>")
def editarTratamiento(id):
    title = "Editar Tratamiento"
    tratamiento_por_id = obtener_tratamiento_por_id(id) 
    return render_template("form_editar_tratamiento.html", title=title, tratamiento=tratamiento_por_id)

@app.route("/tratamiento/update_producto", methods=['POST'])
def updateTratamiento():
    id_edit = request.form['id']
    nombre_edit = request.form['nombre']
    descripcion_edit = request.form['descripcion']
    precio_edit = request.form['precio']
    tipo_edit = request.form['tipo']  # Agrega campo para tipo de tratamiento si es necesario
    actualizar_tratamiento(nombre_edit, descripcion_edit, precio_edit, tipo_edit, id_edit)  # Asegúrate de que esté implementada
    return redirect("/tratamiento")

# Borrar tratamiento
@app.route('/tratamiento/borrar_producto/<int:id>')
def deleteTratamiento(id):
    eliminar_tratamiento(id)  # Asegúrate de que esté implementada
    return redirect("/tratamiento")
# Por ejemplo, en tu vista

@app.route("/cliente/<int:id>")
def mostrarCliente(id):
    title = "Detalles del Cliente"
    cliente = obtener_cliente_por_id(id)  # Asegúrate de que esta función esté definida
    if cliente is None:
        return redirect("/404")  # O maneja el error como desees
    return render_template("cliente.html", title=title, cliente=cliente)

if __name__ == "__main__":
    app.run(debug=True)
