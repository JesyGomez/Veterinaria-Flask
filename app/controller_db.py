from db import conexionMySQL

# Consultas -> CRUD para tratamientos

# Read -> Obtener todos los tratamientos
def obtener_tratamientos():
    """Obtiene todos los tratamientos de la base de datos."""
    try:
        conexion = conexionMySQL()
        with conexion.cursor() as cursor:
            query = "SELECT * FROM tratamientos ORDER BY nombre"  # Ajusta el orden según necesites
            cursor.execute(query)
            result = cursor.fetchall()
        return result
    except Exception as e:
        print(f"Error al obtener tratamientos: {e}")
        return None
    finally:
        conexion.close()

# Read -> Obtener tratamiento por ID
def obtener_tratamiento_por_id(id):
    """Obtiene un tratamiento específico por su ID."""
    try:
        conexion = conexionMySQL()
        with conexion.cursor() as cursor:
            query = "SELECT * FROM tratamientos WHERE id = %s"
            cursor.execute(query, (id,))
            tratamiento = cursor.fetchone()
        return tratamiento
    except Exception as e:
        print(f"Error al obtener tratamiento por ID: {e}")
        return None
    finally:
        conexion.close()

# Create - Insertar nuevo tratamiento
def cargar_nuevo_tratamiento(nombre, descripcion, precio, tipo):
    """Crea un nuevo tratamiento en la base de datos."""
    try:
        conexion = conexionMySQL()
        with conexion.cursor() as cursor:
            query = "INSERT INTO tratamientos (nombre, descripcion, precio, tipo) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (nombre, descripcion, precio, tipo))
            conexion.commit()
            return cursor.lastrowid  # Devuelve el ID del nuevo tratamiento
    except Exception as e:
        print(f"Error al cargar nuevo tratamiento: {e}")
        return None
    finally:
        conexion.close()

# Update -> Actualizar tratamiento
def actualizar_tratamiento(nombre, descripcion, precio, tipo, id):
    """Actualiza un tratamiento existente en la base de datos."""
    try:
        conexion = conexionMySQL()
        with conexion.cursor() as cursor:
            query = "UPDATE tratamientos SET nombre = %s, descripcion = %s, precio = %s, tipo = %s WHERE id = %s"
            cursor.execute(query, (nombre, descripcion, precio, tipo, id))
            conexion.commit()
            return cursor.rowcount  # Devuelve el número de filas afectadas
    except Exception as e:
        print(f"Error al actualizar tratamiento: {e}")
        return None
    finally:
        conexion.close()

# Delete -> Eliminar tratamiento
def eliminar_tratamiento(id):
    """Elimina un tratamiento de la base de datos."""
    try:
        conexion = conexionMySQL()
        with conexion.cursor() as cursor:
            query = "DELETE FROM tratamientos WHERE id = %s"
            cursor.execute(query, (id,))
            conexion.commit()
            return cursor.rowcount  # Devuelve el número de filas afectadas
    except Exception as e:
        print(f"Error al eliminar tratamiento: {e}")
        return None
    finally:
        conexion.close()

# En controller_db.py

def obtener_cliente_por_id(id):
    """Obtiene un cliente específico por su ID."""
    try:
        conexion = conexionMySQL()
        with conexion.cursor() as cursor:
            query = "SELECT * FROM cliente WHERE id = %s"  # Cambia a tu tabla de clientes
            cursor.execute(query, (id,))
            cliente = cursor.fetchone()
        return cliente
    except Exception as e:
        print(f"Error al obtener cliente por ID: {e}")
        return None
    finally:
        conexion.close()
