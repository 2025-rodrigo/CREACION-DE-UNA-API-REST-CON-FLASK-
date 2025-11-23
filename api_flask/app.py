from flask import Flask, jsonify, request

from db import get, post, put, delete

app = Flask(__name__)


# Ruta principal
@app.route("/")
def main():
    return jsonify({"mensaje": "API REST con Flask"})



# GET - Obtener todos los usuarios
@app.route("/users", methods=["GET"])
def users():
    return jsonify(get())



# POST - Crear un usuario
@app.route("/users", methods=["POST"])
def postUser():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Se requiere un cuerpo JSON"}), 400


    nombre = data.get("nombre")
    edad = data.get("edad")
    email = data.get("email")

    if not nombre or not edad or not email:
        return jsonify({
            "error": "Datos incompletos. Se requieren: nombre, edad, email"
        }), 400

    resultado = post(data)
    return jsonify(resultado), 201


# PUT - Actualizar un usuario por ID
@app.route("/users/<int:id>", methods=["PUT"])

def putUser(id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "Se requiere un cuerpo JSON"}), 400

    resultado = put(id, data)
    return jsonify(resultado)



# DELETE - Eliminar un usuario por ID
@app.route("/users/<int:id>", methods=["DELETE"])

def deleteUser(id):
    resultado = delete(id)
    return jsonify(resultado)



# Manejo de rutas inexistentes
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Ruta no encontrada"}), 404


# Ejecución de la app
if __name__ == "__main__":
    app.run(debug=True)
