""" import mysql.connector
from mysql.connector import Error
import bcrypt

def registrar_usuario(nombre, apellido, email, password):
    conexion = None
    cursor = None
    try:
        # Conectar a la base de datos
        conexion = mysql.connector.connect(
            host='192.168.1.4',  # IP del servidor mysql
            database='usuarios',
            user='remote_user',
            password='1234'
        )
        if conexion.is_connected():
            cursor = conexion.cursor()

            # Hash de la password
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
            
            # Decodificar el hash a str
            hashed_password_str = hashed_password.decode('utf-8')

            # Consulta para insertar el usuario
            consulta = "INSERT INTO empleados (nombre, apellido, email, password) VALUES (%s, %s, %s, %s)"
            datos = (nombre, apellido, email, hashed_password_str)

            # Ejecutar la consulta
            cursor.execute(consulta, datos)
            conexion.commit()
            print("Usuario registrado con éxito")
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexion and conexion.is_connected():  # Verificar si conexión tiene un valor y está conectada
            conexion.close()

# Ejemplo de uso:
registrar_usuario('Samuel', 'Jimenez', 'sam_test@example.com', 'samu1234') """

import mysql.connector
from mysql.connector import Error
import bcrypt

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host='172.23.153.171',  # IP del servidor MySQL
            database='usuarios',  # Nombre correcto de la base de datos
            user='remote_user',
            password='1234'
        )
        return conexion
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

def registrar_usuario(nombre, apellido, email, password):
    conexion = None
    cursor = None
    try:
        conexion = obtener_conexion()
        if conexion and conexion.is_connected():
            cursor = conexion.cursor()

            # Hash de la password
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
            
            # Decodificar el hash a str
            hashed_password_str = hashed_password.decode('utf-8')

            # Consulta para insertar el usuario en la tabla empleados
            consulta = "INSERT INTO empleados (nombre, apellido, email, password) VALUES (%s, %s, %s, %s)"
            datos = (nombre, apellido, email, hashed_password_str)

            # Ejecutar la consulta
            cursor.execute(consulta, datos)
            conexion.commit()
            print("Usuario registrado con éxito")
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexion and conexion.is_connected():
            conexion.close()

def obtener_usuarios():
    conexion = None
    cursor = None
    try:
        conexion = obtener_conexion()
        if conexion and conexion.is_connected():
            cursor = conexion.cursor()
            consulta = "SELECT nombre, apellido, email, password FROM empleados"
            cursor.execute(consulta)
            resultados = cursor.fetchall()

            # Mostrar los resultados
            for fila in resultados:
                print(f"Nombre: {fila[0]}, Apellido: {fila[1]}, Email: {fila[2]}, Password: {fila[3]}")
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexion and conexion.is_connected():
            conexion.close()

# Ejemplo de uso:
registrar_usuario('Joanine', 'Cordova', 'joa9@example.com', 'hogaza_manda28')
obtener_usuarios()
