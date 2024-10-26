# pip install pymysql
# pip freeze > requirements.txt
# pip install -r requirements.txt
# conectar bbdd -> host, user, pass, db

import pymysql

# local -> wamp
# host = "localhost"
# user = "root"
# clave= ""
# db="tienda_py"

# remota -> pythonenaywhere
# host = "localhost"
# user = "root"
# clave= ""
# db="veterinaria"

# def conexionMySQL():
#     return pymysql.connect(host=host,user=user,password=clave,database=db)

import mysql.connector

def conexionMySQL():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='veterinaria'
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
