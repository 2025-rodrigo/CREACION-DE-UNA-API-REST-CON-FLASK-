import sqlite3

DB_NAME = "myDB.db"


# Función para conectar a la base de datos
def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row 
    return conn



# READ - Obtener todos los usuarios
def get():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    datos = cursor.fetchall()
    conn.close()


    usuarios = [dict(row) for row in datos]
    return usuarios



# CREATE - Crear un usuario
def post(data):
    nombre = data.get("nombre")
    edad = data.get("edad")
    email = data.get("email")


    if not nombre or edad is None or not email:
        return {"error": "Faltan datos: nombre, edad y email son obligatorios"}

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (nombre, edad, email) VALUES (?, ?, ?)",
            (nombre, edad, email)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return {"error": "El email ya está registrado"}

    nuevo_id = cursor.lastrowid
    conn.close()

    return {"mensaje": "Usuario creado", "id": nuevo_id}



# UPDATE - Actualizar usuario por ID
def put(id, data):
    id = int(id)
    nombre = data.get("nombre")
    edad = data.get("edad")
    email = data.get("email")

    if not nombre or edad is None or not email:
        return {"error": "Faltan datos: nombre, edad y email son obligatorios"}

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "UPDATE users SET nombre=?, edad=?, email=? WHERE id=?",
            (nombre, edad, email, id)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return {"error": "El email ya está registrado por otro usuario"}

    if cursor.rowcount == 0:
        conn.close()
        return {"error": "Usuario no encontrado"}

    conn.close()
    return {"mensaje": "Usuario actualizado correctamente"}


# DELETE - Eliminar un usuario por ID
def delete(id):
    id = int(id)
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE id=?", (id,))
    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return {"error": "Usuario no encontrado"}

    conn.close()
    return {"mensaje": "Usuario eliminado correctamente"}
