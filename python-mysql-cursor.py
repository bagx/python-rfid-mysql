# Bibliotecas
import mysql.connector

# Conexion
cnx = mysql.connector.connect(user='brnxd', password='BAg1222', host='localhost', database='codigoIoT')

# Cursor
cursor = cnx.cursor()

# Query
query = ("SELECT id,nombre,temperatura FROM clima WHERE id=9979;")

# Ejecutar cursor
cursor.execute (query)

res = cursor.fetchall ()

for x in res:
    print (x)