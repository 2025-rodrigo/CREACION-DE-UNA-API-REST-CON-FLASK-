import sqlite3
import os

DB_NAME = "myDB.db"
SQL_FILE = "structureDB.sql"

# Verificar si la base ya existe
if os.path.exists(DB_NAME):
    print(f"La base de datos '{DB_NAME}' ya existe. Se sobreescribirá con el script SQL.")

def create_database():
    # Verificar si el SQL existe
    if not os.path.exists(SQL_FILE):
        print(f"Error: No se encontró el archivo {SQL_FILE}")
        return

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        with open(SQL_FILE, "r", encoding="utf-8") as f:
            sql_script = f.read()

        cursor.executescript(sql_script)
        conn.commit()

        print(f"✔ Base de datos '{DB_NAME}' creada correctamente usando '{SQL_FILE}'.")

    except sqlite3.Error as e:
        print(" Error de SQLite al crear la base de datos:", e)

    except Exception as e:
        print(" Error inesperado:", e)

    finally:
        conn.close()

if __name__ == "__main__":
    create_database()
